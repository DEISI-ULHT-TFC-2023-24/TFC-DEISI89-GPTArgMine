# TFC - Pilot Project Phase

This aggregates the Annotation phase of the Pilot Project, which consisted of two annotators classifying 15 turns into levels from 1 to 5 (1: non-argumentative, 5: argumentative). After the annotations, the IAA was calculated using Krippendorff's Alpha Metric.
In addition, a prompt was made for GPT-4 to do the same thing, the answers were saved and then the IAA was made between the annotators and GPT (in this case also considered an annotator).
The answers were stored in an Excel table (.xlxs)

### Libraries
```python
pip install krippendorff
pip install openpyxl
```
