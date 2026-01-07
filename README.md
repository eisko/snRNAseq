# snRNAseq

Scripts and notebooks to process and analyze single nuclei/single cell data.

Started w/ analyzing downloaded data from Allen, which included single nuclei and single cell data.

## Allen data
- Data used in [Yao et al. 2021](https://www.sciencedirect.com/science/article/pii/S0092867421005018?via%3Dihub)
- Downloaded via [Allen Brain Map](https://brain-map.org/our-research/cell-types-taxonomies/cell-types-database-rna-seq-data/mouse-whole-cortex-and-hippocampus-10x)
- Encompasses Single Cell data (not nuclei)
- Used SMART-Seq V4 or 10x Genomics V2 technology for single cell sequencing
- Animals ages ranged P50-P121, used males and females
- Cells isolated using [Tasic et al., 2018](https://www.nature.com/articles/s41586-018-0654-5) protocol
- Different brain/cortical areas were isolated through microdissection and identified w/ CCFv3 as reference
- Regions labelled ALM were generated w/ SSv4 and for Tasic et al., 2018

Processing of 10xV2 libraries:
```
10xv2 libraries were sequenced on Illumina NovaSeq6000 and sequencing reads were aligned to the mouse pre-mRNA reference
transcriptome (mm10) using the 10x Genomics CellRanger pipeline (version 3.0.0) with default parameters. Cells that had < 1,500
detected genes (with UMI count > 0) were filtered out for downstream processing in each 10x run. Doublets were identified using
a modified version of the DoubletFinder algorithm (McGinnis et al., 2019) and removed when doublet score > 0.3. Doublets were
further removed by first classifying cells into broad cell classes (neuronal versus non-neuronal) based on the co-expression of any
pair of broad class marker genes.
```
