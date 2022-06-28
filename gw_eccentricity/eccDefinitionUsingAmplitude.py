"""
Find pericenters and apocenters using Amplitude.

Part of Eccentricity Definition project.
Md Arif Shaikh, Mar 28, 2022
"""
from .eccDefinition import eccDefinition
from scipy.signal import find_peaks


class eccDefinitionUsingAmplitude(eccDefinition):
    """Define eccentricity by finding extrema location from amplitude."""

    def __init__(self, *args, **kwargs):
        """Init for eccDefinitionUsingAmplitude class.

        parameters:
        ----------
        dataDict: Dictionary containing the waveform data.
        """
        super().__init__(*args, **kwargs)
        self.data_for_finding_extrema = self.get_data_for_finding_extrema()
        self.label_for_data_for_finding_extrema = r"$A_{22}$"

    def get_data_for_finding_extrema(self):
        """Get data to be used for finding extrema location.

        In the derived classes, one need to override this function
        to return the appropriate data that is to be used. For example,
        in residual amplitude method, this function would return
        residual amp22, whereas for frequency method, it would
        return omega22 and so on.
        """
        return self.amp22

    def find_extrema(self, extrema_type="maxima"):
        """Find the extrema in the amp22.

        parameters:
        -----------
        extrema_type: either maxima, pericenters, minima or apocenters
        extrema_finding_kwargs: Dictionary of arguments to be passed to the
        peak finding function. Here we use scipy.signal.find_peaks for finding
        extrema. Hence the arguments are those that are allowed in that function

        returns:
        ------
        array of positions of extrema.
        """
        if extrema_type in ["maxima", "pericenters"]:
            sign = 1
        elif extrema_type in ["minima", "apocenters"]:
            sign = - 1
        else:
            raise Exception("`extrema_type` must be one of ['maxima', "
                            "'minima', 'pericenters', 'apocenters']")

        return find_peaks(
            sign * self.data_for_finding_extrema,
            **self.extrema_finding_kwargs)[0]