Alex Chen, PhD student at UCLA Statistics

Expected Graduation date: December 2025

[Resume_AlexChen](https://github.com/aclheexn1346/aclheexn1346.github.io/blob/7d6868bf593889deb67523628eb1fe441bb13f39/Resume__AlexChen_Oct.pdf)

# Repository of my past/current projects

## Graduate

### PhD Research: Discrete Data De-correlation in Bayesian Networks

![mixed_dda](https://user-images.githubusercontent.com/97409887/236999982-bd3f05ca-c3a0-4b37-a7c8-60c40e633a10.png)

Discrete data, often found in medical or survival data, is difficult to work with, especially in the case of correlated data.  To make use of causal inference methods (which use the i.i.d assumption), we de-correlate the discrete data using a novel method that approximates the Expectation-Maximization (EM) Algorithm.  This method shows improved causal graph estimates over baseline methods that assume independent observations.

We use this method on real RNA-seq data and obtain the causal network between different genes in the data.  To determine if our method improves on traditional naive methods of causal inference, we obtain the likelihood of test data through cross-validation and compare between different methods.

### KDrama recommendations with BERT LLM

As a personal project, I really like Korean drama shows (Kdramas) and am always searching out for another one to watch. This led me to think of an idea to give some movies that I've already watched that I know I like and for an algorithm to let me know what is worth watching next. To use plot points of each show, I web-scraped MyDramaList.com for the top 100 kdramas and used that as my database. Then, I used BERT to understand and vectorize the synopsis. Then, I opted for a nearest-neighbors matching to give me a simple script to give me the recommendations. So far, it's been great!



## Undergraduate

### Undergraduate Research: [Hi-C Chromosome Conformation Capture Prediction using Lasso](https://github.com/aclheexn1346/aclheexn1346.github.io/blob/main/HiC%20Presentation.pdf)

Collaboration with Biostatisticians on finding TADs (Topologically Associating Domains) in Hi-C (https://en.wikipedia.org/wiki/Hi-C_(genomic_analysis_technique)) 25K by 25K big data.  Developed novel method of batch subsampling to fit constrained penalized Lasso regression.  Use of Lasso regression to identify important chromatins to help differentiate between cancer and normal cells.  In addition, due to the high costs of obtaining Hi-C data, we can also make use of the model as an estimate for data that has not been run through the Hi-C analysis, saving potentially 1000s of dollars.  Developed Shiny app to show prediction results from Hi-C data.

<img width="822" alt="Screen Shot 2023-05-08 at 10 02 14 PM" src="https://user-images.githubusercontent.com/97409887/236998581-d3b30e09-d6a5-4d3e-9d45-bd7b3f0bd559.png">

### Datafest 2018 (Won first overall and Best Insight Award): [Using Indeed Job Data to Plan for the Future](https://github.com/aclheexn1346/aclheexn1346.github.io/blob/main/DataFest%20Presentation%20(1).pdf)

<img width="788" alt="Screen Shot 2023-05-08 at 10 18 51 PM" src="https://user-images.githubusercontent.com/97409887/237000899-c874e5b4-1f84-4973-ada0-d58ed46eb348.png">


Use of Indeed job data to identify new metrics and insights to attract new users to Indeed.  Created new metric of relative purchasing power which used outside sources for cost of living data and identified industries as well as education levels which help improve relative purchasing power.  These insights and metrics give Indeed motivation to target younger users by providing insight on the effect of education and industry on salary for user retention.

### [BOAST (Book of Apps for Statistical Teaching)](https://shinyapps.science.psu.edu/): https://shinyapps.science.psu.edu/

<img width="991" alt="Screen Shot 2023-05-08 at 10 07 26 PM" src="https://user-images.githubusercontent.com/97409887/236999225-14f01ec6-8173-4bdd-aab2-d0ab5f9644ec.png">

Collaborating with 9 other students on creating R Shiny applications/dashboards for teaching Statistics concepts in undergraduate classes.  Topics include probability, regression, time series, and more.  Personally created apps on use of Anova and Log Transformation.

###  Datafest 2019 (Won Best Insight Award): [Effectiveness of Self Reporting in Rugby Sevens](https://github.com/aclheexn1346/aclheexn1346.github.io/blob/main/DataFest19.pdf)

<img width="659" alt="Screen Shot 2023-05-08 at 10 05 30 PM" src="https://user-images.githubusercontent.com/97409887/236999029-f7709ba7-5f75-49c0-95a3-c3519885a722.png">

Use of data collected in a professional Rugby team including self-reported wellness, performance, and location data.  Created new metric to evaluate how well players self-reported compared to their performance to evaluate player effectiveness in self-reporting.

### Data Science Capstone Project: [Metaphor Detection with Cross-Lingual Model Transfer](https://github.com/aclheexn1346/aclheexn1346.github.io/blob/main/Metaphor%20Presentation.pdf)

Review of methodology for detecting metaphors in text data.  Practical use in translating between languages, sentiment analysis, and chat bots.  Use of conceptual features such as "Degree of abstractness" or imageability of a word as well as structure of metaphors as an SVO (Subject verb object) or AN (Adjective noun)
Examples:
The snow is a white blanket
He is a shining star
The calm lake was a mirror

Method uses MRC psycholinguistic database to give ratings of abstractness and imageability of words represented as a feature vector compacted via PCA.  Ratings and vector distances for words in the same sentence used to detect metaphors with high accuracy.

<img width="506" alt="Screen Shot 2023-05-08 at 10 05 45 PM" src="https://user-images.githubusercontent.com/97409887/236999042-ef5792cd-7aec-4f82-aa24-9bc809d1d52c.png">

