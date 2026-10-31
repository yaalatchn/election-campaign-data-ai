import pandas as pd
import matplotlib.pyplot as plt

# נתוני פילוח בוחרים לקמפיין
data = {
    'Target_Group': [
        'Youth - Cost of Living',
        'Parents - Education',
        'Retirees - Healthcare',
        'Self-Employed - Taxes',
        'Undecided - Security'
    ],
    'Support_Level': [68, 54, 75, 42, 58],
    'Voter_Count': [12000, 25000, 18000, 9000, 31000]
}

df = pd.DataFrame(data)

# הפקת גרף
plt.figure(figsize=(10, 5))
colors = ['#2b5c8f' if s > 50 else '#d9534f' for s in df['Support_Level']]
bars = plt.barh(df['Target_Group'], df['Voter_Count'], color=colors)

plt.title('Campaign Micro-Targeting: Audience Size & Support Level', fontsize=14)
plt.xlabel('Audience Size (Voters)')
plt.ylabel('Audience Segment')
plt.tight_layout()

# שמירת הגרף כתמונה
plt.savefig('voter_analysis_chart.png')
print("Done! Chart generated successfully.")
