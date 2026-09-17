# Create your views here.

from django.db import connection
from django.shortcuts import render, get_object_or_404
from .models import PollingUnit, AnnouncedPUResult, LGA
from django.db.models import Sum
from django.db import transaction
from django.utils import timezone

def home(request):
    return render(request, "polls/index.html")

def polling_unit(request, polling_unit_id):
    polling_unit = get_object_or_404(
        PollingUnit,
        uniqueid=polling_unit_id
    )

    results = AnnouncedPUResult.objects.filter(
        polling_unit_uniqueid=str(polling_unit.uniqueid)
    ).order_by("-party_score")

    return render(
        request,
        "polls/polling_unit.html",
        {
            "polling_unit": polling_unit,
            "results": results,
        }
    )

def lga_results(request):

    lgas = LGA.objects.filter(
        state_id=25
    ).order_by("lga_name")

    selected_lga = request.GET.get("lga")

    results = []

    selected_lga_name = None

    if selected_lga:

        lga = get_object_or_404(
            LGA,
            lga_id=selected_lga,
            state_id=25
        )

        selected_lga_name = lga.lga_name

        results = (
            AnnouncedPUResult.objects
            .filter(
                polling_unit_uniqueid__in=PollingUnit.objects.filter(
                    lga_id=lga.lga_id
                ).values("uniqueid")
            )
            .values("party_abbreviation")
            .annotate(total_score=Sum("party_score"))
            .order_by("-total_score")
        )

    return render(
        request,
        "polls/lga_results.html",
        {
            "lgas": lgas,
            "results": results,
            "selected_lga_name": selected_lga_name,
        }
    )

@transaction.atomic
def create_polling_unit(request):

    parties = Party.objects.all().order_by("id")

    if request.method == "POST":

        form = PollingUnitForm(request.POST)

        if form.is_valid():

            polling_unit = form.save(commit=False)

            polling_unit.lga_id = int(
                form.cleaned_data["lga_id"]
            )

            polling_unit.ward_id = int(
                form.cleaned_data["ward_id"]
            )

            polling_unit.save()

            for party in parties:

                score = request.POST.get(
                    f"score_{party.partyid}",
                    0
                )

                # The result table uses CHAR(4).
                # LABOUR therefore needs the stored abbreviation LABO.
                party_abbreviation = party.partyid[:4]

                AnnouncedPUResult.objects.create(
                    polling_unit_uniqueid=str(
                        polling_unit.uniqueid
                    ),
                    party_abbreviation=party_abbreviation,
                    party_score=int(score or 0),
                    entered_by_user="admin",
                    date_entered=timezone.now(),
                    user_ip_address=request.META.get(
                        "REMOTE_ADDR",
                        ""
                    ),
                )

            return render(
                request,
                "polls/success.html",
                {
                    "polling_unit": polling_unit
                }
            )

    else:
        form = PollingUnitForm()

    return render(
        request,
        "polls/new_polling_unit.html",
        {
            "form": form,
            "parties": parties,
        }
    )
