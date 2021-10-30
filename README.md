# thesis-2021
Investigate techniques for suppressing grating lobes.  

## Problem Statement
In this project, an investigation is made on how the position, phase shift and amplitude distributions of each antenna element affect grating lobes and how these parameters should be optimized to suppress the grating lobes.

## Objectives 
The aim is to find a fixed element spacing and the resulting phase shift and amplitude distribution that allow for the suppression of grating lobes. This would result in a wider steering range and more efficient antenna. This must be achieved while keeping the half-power beamwidth (HPBW) as narrow as possible and maintaining a superior side lobe level (SLL) and grating lobe level (GLL) compared to a uniformly spaced linear antenna array.

## Grating Lobes
Grating lobes are unwanted lobes that appear when you steer the main beam beyond a critical angle that is determined by the Array Factor (AF). These grating lobes are unwanted because they are wasted energy and cause interference from radiating stations in non-intended directions.


## Summary 
For a uniform, linear antenna array (LAA) spaced half a wavelength apart, the critical angle (CA) at which the lowest SLL becomes larger than −3dB, which qualifies the side lobe as a grating lobes is 33◦ or 57◦ from boresight. This means the steering range of a uniform LAA is 114◦ (63.33%) of the visible space (180◦).

A Genetic Algorithm was designed and deployed to optimize the spacing between a 6 element LAA to suppress the grating lobes that appears at the CA of the uniform LAA. Three solutions were obtained and documented in this report that at the mentioned CA has no grating lobes. The highest SLL of one of the solutions at the CA is 5.045 dB below that of the uniform LAA. This is a 158.1% reduction in the grating lobe level. The half-power beamwidth (HPBW) of these solutions ranges between 3.5◦ to 10◦(9% to 27%) widerthan the uniform LAA. This can be undesirable depending on the application.  

Thereis a clear trade-off between the SLL and HPBW which depends on the intended application. To achieve a narrow HPBW, a wider spacing between antenna elements is required however, this will increase the SLL and decrease the range at which the main beam can besteered because it decreases the distance between grating lobes. To achieve a low SLL, a narrower spaced LAA should be considered but this will increase the HPBW. To ensure grating lobes are suppressed it is shown that the average spacing between antennas should not begreater than half a wavelength although a single spacing between two antennas can be greater than half a wavelength.

## Conclusion

The conclusion drawn from the investigation of grating lobe formed by a LAA is that grating lobes are as aresult of the periodic nature of the AF. This periodicity is as a result of the inter elementspacing of the antennas in a antenna array.

In  a  LAA,  it  is  shown  that  the  element  spacing  affects  the  position  and  distancebetween the grating lobes together with the size of the main beam’s HPBW and SLL.The  phase  shift  and  amplitude  distribution  of  the  signal  entering  the  antennas  onlyaffects the position of the main beam and the SLL and HPBW respectively but not the grating lobes.

It is therefore concluded that a non-uniformly spaced LAA can suppress the grating lobesof the uniform LAA when steered to and beyond the CA. Depending on the specificationsand intended use the steering range can vary between 110◦to 140◦ (61.11% to 77.78%) ofthe visible space. That is an increase of more than 14% in steering capabilities compared to the uniform LAA. The grating lobe is suppressed 158.1% at the CA but at the cost of a 9% to27% increase of the HPBW.