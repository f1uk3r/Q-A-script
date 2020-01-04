print ("""Legend for type
1 for population and sample
2 for retrospective study (all or historical data)
3 for Observational Study
4 for Designed Experiments
5 for Random Samples
6 for analytic study
7 for random, discrete and continuous variable""")


parts = int(input("How many parts: "))

for i in range(parts):
	ty = int(input("Type of this part: "))
    if ty == 1:
        print("A population is the entire collection of objects or outcomes about which data are collected.")
        print("A sample is a subset of the population containing the observed objects or the outcomes and the resulting data.")
    elif ty == 2:
        print("A retrospective study uses either all or a sample of the historical process data from some period of time.")
        print("In most such studies, we are interested in using the data to construct a model relating the variables of interest.")
        print("Primary disadvantages are that some of the important process data often are missing. Reliability and validity of the process data are often questionable. The nature of the proess data often may not allow us to address the problem at hand.")
        print("Using historical data always involves the risk that, for whatever reason, some of the important data were not collected or were lost or were inaccurately transcribed or recorded. Consequently, historical data often suffer from problems with data quality. These errors also make historical data prone to outliers.")
    elif ty == 3:
        print("Observational study simply observes the process or population during a period of routine operation.")
        print("These studies still often provide only limited information about specific relationships among the variables in the system.")
    elif ty == 4:
        print("In a designed experiment, the engineer makes deliberate or purposeful changes in controllable variables (called factors) of the system, observes the resulting system output, and then makes a decision or an inference about which variables are responsible for the changes that he or she observes in the output performance.")
        print("An important distinction between a designed experiment and either an observational or retrospective study is that the different combinations of the factors of interest are applied randomly to a set of experimental units. This allows cause-and-effect relationships to be established")
    elif ty == 5:
        print("The way that samples are selected is important")
        print("A simple random sample of size n is a sample that has been selected from a population in such a way that each possible sample of size n has an equally likely chance of being selected.")
        print("Retrospective data are data of convenience, and they may not reflect current process performance. Data from observational studies are more likely to reflect random sampling, because a specific study is usually being conducted to collect the data.")
    elif ty == 6:
        print("An analytic study is a study or experiment where the conclusions are to be drawn relative to a future population.")
    elif ty == 7:
        print("A random variable is a numerical variable whose measured value can change from one replicate of the experiment to another.")
        print("A discrete random variable is a random variable with a finite (or countably infinite) set of real numbers for its range.")
        print("A continuous random variable is a random variable with an interval (either finite or infinite) of real numbers for its range.")
    elif ty ==8:
        print("If X is a distribution with mean \\mu and variance \\sigma_2")
        print("and Y is a distribution; Y = aX + b")
        print("then")
        print("\\\\E(Y) = E(aX + b) = aE(X) + b = a\\mu +b")
        print("\\\\V(Y) = V(aX + b) = a^2V(X) + 0 = a^2\\sigma^2")