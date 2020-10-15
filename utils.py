from collections import defaultdict

from pandas import DataFrame


def change_method(method):
    methods_to_change = {'Climbing Rope': 'Rope', 'Semi Automatic': 'Semi-Auto', 'Ligature': 'Ligature/Sheet', 'Pistol': 'Handgun', 'Pistiol': 'Handgun', 'Revolver': 'Handgun'}
    return methods_to_change.get(method, method)


def change_cause(cause):
  if type(cause) == str:
    cause = cause.lower().strip()
  causes = {'gunshot wound of head' :'gunshot wound of the head',
  'gunshot wound to the head': 'gunshot wound of the head',
  'shotgun wound of head': 'gunshot wound of the head',
  'strangulation by ligature (hanging)': 'hanging',
  'gunshot wound to head': 'gunshot wound of the head',
  'acute carbon monoxide poisoning': 'carbon monoxide poisoning',
  'shotgun wound to head': 'gunshot wound of the head',
  'gunshot wound of chest': 'gunshot wound of the chest',
  'inhalation of products of combustion': 'asphyxia',
  'shotgun wound to the head': 'gunshot wound of the head',
  'gunshot wounds (2) of head': 'gunshot wound of the head',
  'self-inflicted gunshot wound left chest, suicide': 'gunshot wound of the chest',
  'suffocation': 'asphyxia',
  'gun shot wound to the head': 'gunshot wound of the head',
  'gunshot wound to the head and complications': 'gunshot wound of the head',
  'gunshot wound chest - self-inflicted': 'gunshot wound of the chest',
  'acute oxycodone toxicity': 'oxycodone toxicity',
  'self-inflicted gunshot wound to head': 'gunshot wound of the head',
  'drug intoxication: amitriptyline': 'drug intoxication',
  'drug toxicity: diphenhydramine, doxylamine, meprobamate, morphine (prescription)': 'drug intoxication',
  'drug intoxication: hydrocodone/acetaminophen, tramadol, duloxetine': 'drug intoxication',
  'drug intoxication': 'drug intoxication',
  'drug intoxication - alprazolam': 'drug intoxication',
  'gunshot wound of left upper chest and complications': 'gunshot wound of the chest',
  'ligature hanging and complications': 'hanging',
  'mixed drug poisoning - metoprolol, verapamil,': 'drug intoxication',
  'drug toxicity': 'drug intoxication',
  'gunshot wound of left chest/upper abdomen': 'gunshot wound of the chest',
  'alcohol and drug intoxication: alprazolam, cyclobenzaprine, hydrocodone, fluoxetine': 'drug intoxication',
  'gun shot to the head': 'gunshot wound of the head',
  'self inflicted shotgun wound to the head': 'gunshot wound of the head',
  'quetiapine (seroquel) intoxication': 'drug intoxication',
  'carbon monoxide poisoning': 'carbon monoxide intoxication',
  'shotgun wound of the head': 'gunshot wound of the head',
  'gunshot wounds to the chest': 'gunshot wound of the chest'}
  return causes.get(cause, cause)



def get_sintomas(df: DataFrame, field: str):
  sintomas = defaultdict(list)
  n = len(df)
  for i in range(n):
    ind = df.iloc[i]
    if ind['alcohol']:
      sintomas[ind[field]].append('alcohol')
    if ind['psychosis']:
      sintomas[ind[field]].append('psychosis')
    if ind['anxiety-non-trauma']:
      sintomas[ind[field]].append('anxiety-non-trauma')
    if ind['somatic disorder']:
      sintomas[ind[field]].append('somatic disorder')
    if ind['eating']:
      sintomas[ind[field]].append('eating')
    if ind['bipolar spectrum illness']:
      sintomas[ind[field]].append('bipolar spectrum illness')
    if ind['depression']:
      sintomas[ind[field]].append('depression')
    if ind['interpersonal trauma']:
      sintomas[ind[field]].append('interpersonal trauma')
    if ind['PD-Cluster C-anxiety']:
      sintomas[ind[field]].append('PD-Cluster C-anxiety')
    if ind['PD-Cluster B-emotional']:
      sintomas[ind[field]].append('PD-Cluster B-emotional')
    if ind['PD']:
      sintomas[ind[field]].append('PD')
    if ind['Impulse control disorder']:
      sintomas[ind[field]].append('Impulse control disorder')
    if ind['obesity']:
      sintomas[ind[field]].append('obesity')
    if ind['cardiovascular']:
      sintomas[ind[field]].append('cardiovascular')
    if ind['COPD']:
      sintomas[ind[field]].append('COPD')
    if ind['asthma']:
      sintomas[ind[field]].append('asthma')
    if ind['immune-autoimmune']:
      sintomas[ind[field]].append('immune-autoimmune')
  
  return sintomas
