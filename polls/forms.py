class PollingUnitForm(forms.ModelForm):

    lga_id = forms.ChoiceField(
        label="Local Government"
    )

    ward_id = forms.ChoiceField(
        label="Ward"
    )

    class Meta:
        model = PollingUnit

        fields = [
            "polling_unit_id",
            "lga_id",
            "ward_id",
            "polling_unit_number",
            "polling_unit_name",
            "polling_unit_description",
            "lat",
            "long",
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["lga_id"].choices = [
            ("", "-- Select LGA --")
        ] + [
            (lga.lga_id, lga.lga_name)
            for lga in LGA.objects.filter(
                state_id=25
            ).order_by("lga_name")
        ]

        self.fields["ward_id"].choices = [
            ("", "-- Select Ward --")
        ] + [
            (ward.ward_id, ward.ward_name)
            for ward in Ward.objects.all().order_by("ward_name")
        ]
