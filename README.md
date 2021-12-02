# DS-5100 Group Project

Uyen Nguyen (gmd8sq) \
Andy Ortiz (eao7r) \
Lee Ann Johnson (lj6gd) \
JD Pinto (jp5ph)

## Introduction 
  After breast cancer and prostate cancer, lung cancer is the second most diagnosed cancer in the United States (U.S.) for both men and women. In 2021, approximately 235,760 new cases will be diagnosed (SEIGEL, 2021). Unfortunately, lung cancer remains the leading cause of cancer-related deaths with approximately 131,880 new deaths estimated for 2021 (SEIGEL, 2021). Regardless of survival, a significant number of individuals with lung cancer receive cancer care each year.
  Although lung cancer claims the lives of more Americans than any other type of cancer, relatively little is understood about lung cancer survivors when compared to other types of cancer where individuals live longer after diagnosis. Relatively short survival times after a diagnosis have limited studies in this area. Individuals are typically considered by be survivors of cancer beginning at the time of a cancer diagnosis. Due to the high number of new lung cancer cases, and thus high number of new lung cancer survivors each year, it is vital to understand lung cancer survivorship outcomes. 
  The overall purpose of this project was to examine, among individuals with lung cancer, potential disparities in survivorship care. More specifically, in a nationally representative sample of individuals with lung cancer, we will 1) describe the demographics, physical, and mental health characteristics, 2) examine associations between demographics, physical, and mental health characteristics and the survivorship outcomes (cancer care summaries, written cancer care summaries, and health insurance coverage), 3) model which demographic physical, and mental health characteristics predict survivorship outcomes. 


## Data Set
  To explore cancer survivorship outcomes in a nationally represented sample of individuals with lung cancer, the Behavioral Risk Factor Surveillance System (BRFSS) data set was selected. This dataset is created through an annual telephone-based survey collected in each U.S. state and territory. The primary questions are standardized between states, and included information pertaining to use of preventative services, health-related risk behaviors, and chronic health conditions. In addition to the standard questions, states can opt to administer other approved and standardized health-related modules. 
  
	BRFSS data is published annually on the Centers for Disease Control website (https://www.cdc.gov/brfss/index.html). Published materials for each year include the questionnaires, a data dictionary that identifies questions and answer codes, and the data. All data are deidentified and freely available for download. Each year of data is available as a separate file. For this project, to ensure an adequate sample size of individuals diagnosed with lung cancer, data from the following years were selected: XXXXXXXXXXX. 

## Data Structure
The data structure used for this project is a ??? 2-D array????

## Data Pre-processing

Since this is a rather big dataset, we decided to filter out survery data that only has lung cancer. We initially did this for 2020, but we went back and added several other years to yield a larger sample dataset in order to train our logistic regression. But inital data exploratory from the dataset of only 2020 painted the picture:

<p align="center">
  <img src="Images/hist.PNG">
</p>

Which confirmed our assumption of lung cancer being prevalent in the middle age to older adult population. The histogram showed a left skewed distribution, capturing the more older adults with lung cancer as opposed to younger adults being interviewed from the survey. 

We also wanted to visualize states that conducted topics on lung cancer so we produced the plot:

<p align="center">
  <img src="Images/states.PNG">
</p>

This plot can be interacted via the lung cancer sandbox script in our [Scripts](https://github.com/yoowhyeeen/DS-5100/tree/master/Scripts) folder. The plot displays the value and the abbreviation of the state when hovered on (available in the lung cancer sandbox ipynb) 

Furthermore, we came up with an initial logistic regression of the variable CSRVSUM with respect to sex, age groups, education levels, and marital status, which gave us:

<p align="center">
  <img src="Images/csrvsum wrt sex-age-edu-marital.PNG">
</p>

As well as a confusion matrix and score:

<p align="center">
  <img src="Images/cm%20csrvsum%20wrt%20sex-age-edu-marital.PNG">
</p>

We have more visuals and results on the way as our group wraps up on final details and interpretation. We are excited to share our findings with all of you soon!

## Experimental Design 
For this project, we propose to fit a MLRM onto the selected data set to predict both cancer survivorship outcomes for 2020 and in subsequent years when the survivorship question module is administered. The following steps briefly outline the proposed project methodology:

- [x] Download the dataset LLCP2020.xpt from CDC
- [x] Create a colab notebook 
- [x] Import the necessary packages (google.colab, pandas, etc.)
- [x] Explore and clean the dataset
- [x] Visualize the data
- [x] Develop a hypothesis
- [x] Outline our assumptions
- [ ] Check our assumptions
- [x] Fit the regression model
- [x] Interpret the results 
- [ ] Write code for user interaction with graphs and plots

## Project Management
Roles: Uyen Nguyen (Programmer), Andy Ortiz (Programmer), JD Pinto (Project Manager), Lee Ann Johnson (Data interpretation/Writing/Editing)

- [x] Milestone 1 (Week 1-2): Choose predictor and response variables, develop hypotheses, outline assumptions, check assumptions (if assumptions fail, remedy the assumptions or find alternative approach to analysis).  

- [x] Milestone 2 (Week 3-4): Fit the model, extract insights from graphs, write unit tests, draw conclusions  

- [ ] Milestone 3 (Week 5-6): Debug and test code, organize visualizations

- [ ] Milestone 4 (Week 7-8): Conclude all steps from above and produce a presentation/video. 

## Results
Based on analysis output, including graphs, we will interpret the results and contextualize the findings within the context of cancer survivorship. Meaningful graphs will be created.

## Testing 
For this proposal, to ensure accuracy of the code and robustness of results,  we will use exception testing and unit tests.

## Conclusions 
The goal of this proposal is to:

1. Use our tool to apply the model across different years of data and 
2. Explore health equity in cancer survivorship outcomes. Findings can provide feedback to states about trends in cancer survivorship as well as provide evidence as to the importance of including these questions in future iterations of the BRFSS surveys. 

