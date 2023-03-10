# Hotel Effectiveness Night Audit Entry Reporter

Partially automates the process of creating reports for night audit entry for housekeeping.

## Dependecies

WILL ONLY WORK WITH EXCEL FILES FROM INFOR HMS. Download the excel file directly from Housekeeping Assignment page. Will need to filter out unassigned rooms.\
Packages:\
Pandas
```
Pandas
```
Use package mangaer [pip](https://pip.pypa.io/en/stable/)

```bash
pip install Pandas
```


## Usage

This version is set to a specific hotel.

To change room type change global variables on HKRECON.py

```python
kings = ['Room types here']
queens = ['Room types here']
suitesK = ['Room types here']
SuitesS = ['Room types here']
suitesQ = ['Room types here']
```

To change points/credits

```python
if points == credit_values_here
```
