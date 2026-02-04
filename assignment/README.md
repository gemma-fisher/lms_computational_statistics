## MRC LMS - Introduction to computational statistics

### Jesús Urtasun Elizari, MRC LMS & RCDS ICL

LMS email address `Jesus.Urtasun@lms.mrc.ac.uk`

ICL email address `jurtasun@ic.ac.uk`

<img src="/readme_figures/ukri_lms_logo.png" width = 700>

### Assignment. Analysis of expression and methylation data.

In this assignment, we work with two real biological datasets generated using high-throughput sequencing technologies. The goal is to combine the descriptive statistics, probability theory and hypothesis testing tools learned through the course on realistic genomics examples.

---

### 1. DNA methylation data (EM-seq)

The EM-seq dataset contains **DNA methylation measurements** across genomic regions.

- Each row corresponds to a genomic location (`chr_start_end`).
- Samples were grown under two environmental conditions:
  - **200 µM** (control condition)
  - **3 µM** (nutrient-deprived condition)
- Each condition has **two biological replicates**.

For each replicate, two values are provided:
- Number of **C bases** (`nC`), representing methylated cytosines
- Number of **T bases** (`nT`), representing unmethylated cytosines converted during the EM-seq protocol

From these counts, we compute a **methylation score** for each genomic region:

\[
\text{methylation score} \; s = \frac{nC}{nC + nT}
\]

This score:
- ranges between **0 and 1**,
- represents the **fraction of methylated cytosines** at that genomic location.

Scores are computed **per replicate**, and then **averaged across replicates** for each condition.

We then:
- compute basic summary statistics (mean, median, variance, standard deviation),
- and visualize the distributions using boxplots, violin plots, and histograms.

At this stage, we are only **describing the data**, not testing for differences.

---

### 2. Gene expression data (RNA-seq)

The RNA-seq dataset contains **gene expression counts**.

- Each row corresponds to a gene (Ensembl ID).
- Samples were grown under the same two conditions:
  - **200 µM control**
  - **3 µM deprived**
- There are **three replicates per condition**.
- Each column contains raw read counts, representing how many sequencing reads were assigned to each gene.

Replicates are **pooled** by concatenation rather than averaged, producing one large distribution per condition.

Because raw RNA-seq counts are:
- non-negative,
- highly skewed,
- and span several orders of magnitude,

we apply a **log transformation** to improve visualization:

\[
x_{\text{log}} = \log(x + 1)
\]

where:
- \(x\) is the raw read count,
- adding **1** avoids taking the logarithm of zero.

The log transformation:
- compresses large values,
- spreads out small values,
- and makes distributions easier to compare visually.

As with the EM-seq data, we then compute:
- mean, median, variance, and standard deviation (manually and using NumPy),
- and visualize the data using boxplots, violin plots, and histograms.

---

Overall, these exercises introduce:
- how biological data are structured,
- how simple mathematical formulas summarize sequencing data,
- and how visualization complements numerical summaries.

Formal hypothesis testing is introduced in later chapters.