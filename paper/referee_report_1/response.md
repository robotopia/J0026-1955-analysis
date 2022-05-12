Dear editor,

We thank the referee for the many detailed comments, which we have tried to address in this revised version. In many instances, the referee asked for a more thorough analysis, particularly surrounding the nulling phenomenon, which -- now that the paper is being submitted to the main journal (instead of Letters) there has been room to include, and we believe the paper is much better for it. In a few cases, however, we have deferred the suggested deeper analysis until the planned follow-up paper, which will benefit from an expanded data set and a wider frequency coverage. Please find our detailed response to the referee's comments below.

Sincerely,

~/Sam

-------------------------------------------------------

1. The observation, theory and scientific application of pulsars are not fully introduced and need to be expanded. For example, This, along with tests of general relativity (e.g. Kramer et al. 2006; Miao et al. 2021, ApJ, 921, 114), pulsar timing arrays for gravitational wave detection (e.g. Manchester et al. 2013), pulsar braking and magnetospheric dynamics (e.g. Gao et al. 2017, 849,19, Wang et al. 2020, Universe, 6, 63) the neutron star equation of state (e.g. Antoniadis et al. 2013 Science 340 448, Pang, et al. 2021, ApJ, 922,14), and other pulsar science applications, motivates efforts to find new pulsars via large scale pulsar surveys, which continue to be conducted up to the present day.

  * We have added in the suggested text and references.

2. There are some peculiar but interesting subpulse drifting pulsars, such as J1727−2739， J1822-2256 and the Vela pulsar, which could be missed in this paper. Please refer to articles: Wen et al. 2016, A&A 592, A127; Wen et al. 2021,ApJ,900,168; Janagal, Parul et al. 2022, MNRAS, 509, 4573.

  * We have added the text "J0026−1956 is also found to contain null sequences, a phenomenon which is known to be connected to drifting behaviour, originally noticed by (Lyne & Ashworth 1983), and further attested by recent studies of PSRs J1727−2739 (Wen et al. 2016), J1822−2256 (Janagal et al. 2022), and the Vela pulsar (Wen et al. 2020)" to the introduction.

3. The authors referred to the RS model (Ruderman & Sutherland 1975). Although the RS model successfully explains the formation mechanism of drift subpulse, it is difficult to explain the complex drift subpulse phenomena, such as the erratic drift rate, the change of drift direction, and the transition between various drift states. For this reason, many researchers have developed the RS model to explain various special subpulse drifting phenomena (e.g. Gil & Sendyk 2000,ApJ, 541,351; Qiao et al. 2004, ApJ,616, L127).

  * We have edited the text to read "Such pulsars exist, and several extensions have been proposed over the years to account for them. For example, Gil & Sendyk (2000) suggest that a quasi-central spark can account for (non-drifting) core components in profiles, and the well-known phenomenon of bi-drifting may be explained by presence of an inner annular gap (Qiao et al. 2004), an inner acceleration gap (Basu et al. 2020), or non-circular spark motions (Wright & Weltevrede 2017). Such extensions are typically developed to explain specific drifting behaviors that are observed in a relatively small subset of pulsars, and there still lacks a single, comprehensive theory that can describe all drifting behaviors. [newline] Pulsars that both show complicated drifting behavior and which are bright enough for single pulse analysis, are relatively rare."

4. Which bright source was used for phase or amplitude calibration? Is it possible to convert the flux into absolute amplitude in the figures instead of arbitrary unit?

  * On inspection, it turns out that all of our observations were calibrated on 3C444. I have edited the text to read "Each observation was individually calibrated using observations of 3C444 taken within ∼2 hours of the respective target observations. The calibration solutions were obtained using the Real Time System software (Mitchell et al. 2008)."
  * Getting reliable absolute flux calibration is challenging for the MWA because of its large, complex primary beam. A fuller investigation of the absolute brightness of the pulsar is intended for a follow-up paper, for which we have also recently acquired observations at higher frequencies (uGMRT), and which we will use for spectral analysis.

5. Please clarify the technical principle of the PSRCHIVE's pdmp to determine period and DM.

  * The following text has been added to Section 2.2: "This routine performs a brute-force grid search in both period and DM parameter space, and returns the period and DM that yields the highest profile signal-to-noise."

6. In single-pulse study, the radio frequency interference can act to reduce the signal-to-noise ratio. Considering the weak nature of single pulses, it is necessary to subtract away or mask undesirable signals from the data before single-pulse analysis. Please describe the RFI mitigation technique you used.

  * We have added the text: "The MWA is located in a very radio quiet location, and no significant RFI was found in the beamformed data."

7. Please indicate the flux value in the ordinates of Figure 1 for each averaged pulse profiles.

  * Since we do not have reliable absolute fluxes at this stage, Figure 1 shows normalised profiles. We have added "peak-normalised" to the caption of the figure.

8. It is difficult to determine whether nulling or just weak emission exists in this pulsar only from Figures 2 and 3. The pulse energy distribution is a statistical way to characterize the nulling behavior (Wen et al. 2020, ApJ, 904, 72).

  * We have now included pulse energy distributions for all six observations (see also our response to points 12 & 13 below). From the distributions of the two 20-min observations in which the pulsar was not detected in a periodicity search, we conclude that if there is any weak emission, it must fall far below the MWA's detection threshold. The new text discussing the pulse energy histograms can be found in Section 3.1.

9. Is there any temporal evolution of nulling fraction from follow-up observations and archival MWA data? Is it possible that the constraints on the nulling fraction might be reported in this paper?

  * It still remains the case that only a limited number of archival MWA data sets have been processed and analysed (being those which are presented in this paper). We do expect to get better constraints of the nulling fraction once more data have been processed, but this remains outside the scope of the present initial analysis, and will be presented in the planned follow-up paper.

10. The nulls from a few pulsars does not seem to be random, but show well-defined periodicity (e.g. Herfindal & Rankin 2007, MNRAS, 380, 430; Wang et al. 2021, ApJ, 923, 259). Try to examine whether the periodicity in the transitions between null and burst states is present in this pulsar.

  * We have examined the fluctuation spectra for each of our data sets, but find no evidence of periodicity in the null-burst transitions. To be clear, the observations which showed any discernible low-frequency features at all were 1226062160, 1274143152 and 1283104232. For the latter two, the low-frequency feature occurred in the first (non-DC) frequency bin, which is not surprising, as this only reflects the fact that only a single (long) nulling sequence was present in both. Similarly, the low-frequency feature in 1226062160's spectrum occurs in the second (non-DC) bin, corresponding to the presence of two main (long) null sequences. In all cases, the ratio of observation length to null length is too small to make any assertions about whether the observed null lengths are typical, or whether they are periodic or quasi-periodic. This will be explored in the future once more (and longer) follow-up observations have been made.

11. The pulsar switches between null and burst states with short and long timescales, which provides an important clue to scrutinize various nulling mechanism models. The null and burst length histograms are required.

  * We completely agree that a deeper study of the state transitions has great potential to shed light on the nulling mechanism. However, the working definition of nulls used in this work makes the suggested null and burst length analysis problematic, because no distinction is made between "true" nulls and pseudo-nulls. Consequently, long burst sequences that are likely continuous under a stricter definition of nulls are, in this analysis, frequently interrupted by (likely) pseudo-nulls (as can be clearly seen in the new Figure 2). This effectively alters the null and burst length histograms dramatically. Therefore, we feel that histograms of the null/burst lengths under the current definition would not contain as much useful information about the nulling mechanism as hoped. A deeper analysis is certainly required, but, we feel, outside the scope of the present paper and will be included in the follow-up paper.

12. Whether the observed nulls are true or just weak emission below the detection threshold of the telescope? To answer this question, the analysis of integrated pulse profile obtained from all classified nulls is necessary.

  * These are now included with the profiles in Figure 1.

13. There was no detection in the two 20-min MWA observations made via periodicity search. A few pulsars were reported to exhibit sporadic, strong single pulses coexisting with a periodic weak emission in the duration of weak mode (e.g. PSR B0826-34). Does J0026-1956 has the similar emission behavior? You'd better try single-pulse search technique on the two observations.

  * We formed pulsestacks of the two 20-min observations and found a small amount of relatively faint emission in them that is just visible in the pulse stack. Accordingly, we have promoted these two observations to the same standing as the original four, included them in Table 1 and Figure 2, and performed all the same analyses on them. The lack of significant emission in these two observations means that the main conclusions of our nulling analysis are essentially unchanged. There are many places throughout the text that have been updated accordingly, which are marked in bold as usual.

14. The LRFS in Figure 6 clearly presents the drifting feature at a frequency of ~0.03 cycles/period in the on-pulse window. In addition, a wide modulation feature with frequency ranging from 0.05-0.1 cycles/period is detected in the leading emission component. The corresponding feature with weak power in the 2DFS is also discernible.

  * These extra details are now more explicitly spelled out in the caption to the LRFS/2DFS figure. We have also expanded slightly on the interpretation of the diffuse component (as a possible connection to Mode B) in the last part of Section 3.2.4.

15. The polarized pulse profiles for different drift modes provide an important clue to reveal the triggering mechanism of mode changing. Is there any difference between averaged pulse profiles by integrating pulses for different drift modes?

  * Unfortunately, we do not yet have reliable polarization for these data sets, but intend to include them in the planned followup paper.
  * We plotted, but have not included, the modal profiles. Visually, there is no significant difference between the profiles of the different modes. The limiting factor here is the relative paucity of Mode B sequences, making the Mode B profiles too noisy to meaningfully compare with the Mode A profiles. However, to the extent we are able to say, they appear to have the same basic shape (two just-resolved components, with the leading component slightly brighter than the trailing component.

16. The observed different subpulse drift modes and the slowly changing in drift rate may be an indication of a local change in the electromagnetic field configuration in the gap. A lot of theoretical modes have been proposed, such as van Leeuwen et al. 2003, A&A, 399, 223; Smith et al. 2005, A&A, 440, 683; Yuen, 2019, MNRAS, 486, 2011.

  * This is indeed our current feeling, and we have amended the relevant paragraph in the Discussion slightly to include the wording suggested by the referee. We have included the van Leeuwen and Yuen references, but could not identify the Smith reference.

17. To our knowledge, no model can satisfactorily explain the observed subpulse drift characteristics for different pulsars. In the future, the multi-frequency study will be required.

  * We wholeheartedly agree! Our next study plans to include both GMRT and Parkes data, covering a wide frequency range.
