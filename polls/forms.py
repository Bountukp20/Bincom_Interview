class PollingUnitForm(forms.ModelForm):

    lga_id = forms.ModelChoiceField(
        queryset=LGA.objects.filter(state_id=25).order_by("lga_name"),
        empty_label="Select LGA"
    )

    ward_id = forms.ModelChoiceField(
        queryset=Ward.objects.all().order_by("ward_name"),
        empty_label="Select Ward"
    )

    class Meta:
        model = PollingUnit

        fields = [
            "polling_unit_id",
            "ward_id",
            "lga_id",
            "polling_unit_number",
            "polling_unit_name",
            "polling_unit_description",
            "lat",
            "long",
        ]
