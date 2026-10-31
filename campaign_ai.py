import matplotlib.pyplot as plt
import pandas as pd

# נתוני פילוח בוחרים מותאמים לקונטקסט הישראלי
data = {
    'Target_Group': [
        'Young Adults & Students - Cost of Living & Rent',
        'Reserve Soldiers & Families - Civil Rights & Grants',
        'Young Families (Periphery) - Affordable Housing',
        'Small Business Owners - Economic Relief & Bureaucracy',
        'Undecided / Swing Voters - National Security & Trust'
    ],
    'Support_Level': [68, 74, 52, 41, 57],
    'Voter_Count': [18500, 24000, 31000, 11500, 42000]
}

df = pd.DataFrame(data)

# הגדרת עיצוב נקי
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, ax = plt.subplots(figsize=(12, 6))

colors = ['#1d3557' if s >= 50 else '#e63946' for s in df['Support_Level']]
bars = ax.barh(df['Target_Group'], df['Voter_Count'], color=colors, height=0.6, edgecolor='none')

# הוספת תוויות נתונים בקצה כל עמודה
for bar, support, count in zip(bars, df['Support_Level'], df['Voter_Count']):
    ax.text(
        bar.get_width() + 600,
        bar.get_y() + bar.get_height() / 2,
        f"{count:,} voters  |  {support}% support",
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold',
        color='#333333'
    )

# כותרות והתאמת צירים
ax.set_title('Campaign Micro-Targeting: Segment Size & Support Level (Israel 2026)', fontsize=14, fontweight='bold', pad=18)
ax.set_xlabel('Audience Size (Estimated Registered Voters)', fontsize=11, labelpad=10)
ax.set_ylabel('Target Audience Segment', fontsize=11)
ax.set_xlim(0, max(df['Voter_Count']) * 1.35)

# הסרת גבולות מיותרים
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# הוספת מקרא
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, color='#1d3557', label='Favorable Segment (Support >= 50%)'),
    plt.Rectangle((0, 0), 1, 1, color='#e63946', label='At Risk / Skeptical Segment (< 50%)')
]
ax.legend(handles=legend_elements, loc='lower right', frameon=True, facecolor='white', framealpha=0.9)

plt.tight_layout()
plt.savefig('voter_analysis_chart.png', dpi=300)
print("Updated realistic Israeli campaign chart generated successfully!")
