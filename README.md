# Increment_Threshold_Experiment_VisualField
An experiment measuring increment thresholds using square stimuli and Pokorny &amp; Smith's (1997) pulsed- and steady-pedestal paradigms under hypothetical parvocellular- and magnocellular-biased conditions. The adaptive QUEST (Watson &amp; Pelli, 1983) is used to more efficiently and accurately measure the thresholds.

![GitHub last commit](https://img.shields.io/github/last-commit/JaeseonSong/Increment_Threshold_Experiments)

> This experiment was created using PsychoPy v.2021.2.3 for a monitor with an 85-Hz refresh rate and a screen resolution of 800 x 600. The monitor was calibrated using a Photo Research PR-650 Spectrophotometer, and the viewing distance was 70 cm.

## How To Use
Download both "VF_conds.py" and "Increment_Thresholds_VF.py" into the same folder of your choice. You'll need PsychoPy (v.2021.2.3 or later version) to run the code. Run "Increment_Thresholds_VF.py" to start the experiment.

You can clone your repository to create a local copy on your computer and sync between the two locations.

[Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Stimuli and Procedure

![Procedure-vf](https://user-images.githubusercontent.com/118466581/234408495-140dba17-1f58-41d2-b8bb-27338b9e986d.png)

The experiment has 48 conditions, which are pseudorandomized (check "VF_conds.py"). These conditions involve stimuli presented in either the upper-right or lower-left visual field at 3.6° eccentricity. Stimuli are either red or green, and have 6 Michelson contrasts ranging from 0.0 to 0.64. The experiment uses the pulsed- and steady-pedestal paradigms (Pokorny & Smith, 1997).

During the pre-adaptation period, which lasts for 30 seconds (3 seconds for top-ups), the participant can use the fixation guides to fixate the center of the screen. After the pre-adaptation period, one of the squares in the two-square array is randomly chosen to have its luminance incremented and serve as the test square, while the other square serves as the reference square. The test period lasts for 35.3 ms and is followed by the pedestal contrast in the steady-pedestal paradigm or the surround luminance in the pulsed-pedestal paradigm.

The observer's task is to identify which square is brighter using a two alternative forced choice (2AFC) method. Depending on the answer, the change in test square luminance is adjusted in the next step using the adaptive QUEST procedure (Watson & Pelli, 1983). Contrast discrimination thresholds are obtained by fitting a Weibull psychometric function to the test half's contrast increment yielding 75% of correct responses.

## Links

This code is used for a study presented at the Vision Sciences Society (VSS) 2023 Meeting. The study is titled "Further examination of the pulsed- and steady-pedestal paradigms under hypothetical parvocellular- and magnocellular-biased conditions." 
For more information, go to: [VSS 2023 meeting](https://www.visionsciences.org/presentation/?id=4837)
