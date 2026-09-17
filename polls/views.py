# Create your views here.

from django.db import connection

from django.shortcuts import render, get_object_or_404

from .models import PollingUnit, AnnouncedPUResult


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
