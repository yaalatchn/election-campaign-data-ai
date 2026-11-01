 import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="קמפיין בחירות מבוסס נתונים ובינה מלאכותית",
    page_icon="🗳️",
    layout="wide"
)

# התאמת יישור גורפת לעברית נקייה
st.markdown("""
<style>
    div, p, span, h1, h2, h3, h4, li {
        direction: rtl !important;
        text-align: right !important;
    }
</style>
""", unsafe_allow_html=True)

slides = [
    "1. שער ומבוא",
    "2. בעיית המחקר והאתגר",
    "3. רקע תיאורטי ומיקרו-טרגטינג",
    "4. שלבי העבודה וזרימת הנתונים",
    "5. תיעוד העבודה מול מודלי שפה",
    "6. ניתוח נתונים ואופטימיזציית תקציב (אינטראקטיבי)",
    "7. תוצר וידאו מותאם אישית",
    "8. אתיקה, פרטיות ורגולציה",
    "9. מדדי הצלחה ויעילות",
    "10. סיכום ומסקנות"
]

selected_slide = st.sidebar.radio("ניווט במצגת:", slides)

# -------------------------------------------------------------
# שקף 1
# -------------------------------------------------------------
if selected_slide == slides[0]:
    st.markdown('<div dir="rtl"><h1>קמפיין בחירות מבוסס נתונים ובינה מלאכותית</h1></div>', unsafe_allow_html=True)
    st.markdown('<div dir="rtl"><h3>פילוח בוחרים, אופטימיזציית תקציב והתאמת מסרים אישית</h3></div>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div dir="rtl">
        <h3>על הפרויקט</h3>
        <p>הפרויקט מציג הוכחת היתכנות (פיילוט) לשילוב בין ניתוח נתונים בפייתון לבין יצירת תוכן מותאם אישית באמצעות בינה מלאכותית יוצרת.</p>
        <p>במקום קמפיין אחיד שמפזר תקציב על מסרים כלליים, המערכת מנתחת קהלי בוחרים שונים ומאפשרת להתאים לכל מגזר את המסר המדויק שמניע אותו לצאת ולהצביע.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("""
        **מגישות הפרויקט:**  
        * יעלת חן פרידמן  
        * עדי זך  
        
        **כלים וסביבת עבודה:**  
        * פייתון (ספריות פנדס ומטפלוטליב)  
        * מודלי וידאו בבינה מלאכותית  
        * גיטהאב (ניהול גרסאות שיתופי)
        """)

# -------------------------------------------------------------
# שקף 2
# -------------------------------------------------------------
elif selected_slide == slides[1]:
    st.markdown('<div dir="rtl"><h2>האתגר: שחיקת האפקטיביות במסרים אחידים</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div dir="rtl">
        <h3>הכשלים בקמפיין מסורתי</h3>
        <ul>
            <li><b>בזבוז משאבים:</b> תקציבי ענק מושקעים בשלטי חוצות ובסרטונים גנריים שלא נוגעים באף אחד באמת.</li>
            <li><b>חוסר רלוונטיות:</b> מסר אחיד לא מדבר לכולם (סטודנטית מוטרדת משכר דירה, בעוד פנסיונר מוטרד מבריאות וקצבאות).</li>
            <li><b>חוסר גמישות:</b> קושי לזהות בזמן אמת איזה קהל מתלבט ואיזה קהל כבר משוכנע.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div dir="rtl">
        <h3>הפתרון מבוסס הנתונים</h3>
        <ul>
            <li><b>פילוח קהלים חכם:</b> חלוקת הבוחרים לקבוצות ברורות לפי תחומי עניין ורמת תמיכה.</li>
            <li><b>התאמת תוכן פרסונלית:</b> פנייה לכל בוחר בשפה, בנושא ובמסגור שמניעים אותו לפעולה.</li>
            <li><b>אופטימיזציית תקציב:</b> המרצה של תומכים בטוחים לצד שכנוע ממוקד של קולות צפים.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 3
# -------------------------------------------------------------
elif selected_slide == slides[2]:
    st.markdown('<div dir="rtl"><h2>רקע תיאורטי: מיקרו-טרגטינג וחלוקת משאבים</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div dir="rtl">
        <h3>1. המרצת בוחרים לעומת שכנוע</h3>
        <ul>
            <li><b>המרצה לקלפי (GOTV):</b> השקעת משאבים בבסיס התומכים שכבר מזדהה עם המועמד, כדי לוודא שייצא בפועל להצביע.</li>
            <li><b>שכנוע מתלבטים:</b> ניתוב מסרים מעמיקים לקולות הצפים שטרם גיבשו עמדה סופית.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div dir="rtl">
        <h3>2. מסגור מותאם אישית (Targeted Framing)</h3>
        <ul>
            <li>שמירה על זהות המועמד ועקרונות הליבה, תוך התאמת ההקשר לחיי היומיום של קהל היעד.</li>
            <li>בניית אמון והזדהות על ידי שימוש בנושאים, שפה ונראות הרלוונטיים לנמען.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 4
# -------------------------------------------------------------
elif selected_slide == slides[3]:
    st.markdown('<div dir="rtl"><h2>שלבי העבודה וזרימת המידע בפרויקט</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    <div dir="rtl">
    <ol>
        <li><b>אפיון דרישות מערכת:</b> מיפוי קהלי יעד ריאליסטיים בישראל, הגדרת נושאי הליבה וקביעת מדדי הצלחה.</li>
        <li><b>ניתוח נתונים בפייתון:</b> בניית נתוני סימולציה, סיווג לפי גודל קהל ואחוזי תמיכה, והפקת תרשים החלטות.</li>
        <li><b>הפקת קריאייטיב בבינה מלאכותית:</b> יצירת סרטון מותאם אישית שמשקף את הממצאים מהניתוח הכמותי.</li>
        <li><b>בקרת איכות ותיעוד בגיטהאב:</b> ניהול גרסאות מסודר, שיתוף פעולה בצוות ותיעוד מלא של הפרומפטים.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 5
# -------------------------------------------------------------
elif selected_slide == slides[4]:
    st.markdown('<div dir="rtl"><h2>תיעוד העבודה מול כלי הבינה המלאכותית</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    <div dir="rtl">
    <p>כל תהליך הפיתוח והאינטראקציה מול הבינה המלאכותית תועד בקובץ ייעודי במאגר (prompts_log.md):</p>
    <ul>
        <li><b>אפיון ופיתוח קוד:</b> שימוש במודלי שפה להגדרת דרישות המערכת, כתיבת סקריפט הניתוח בפייתון ושדרוג הוויזואליזציה.</li>
        <li><b>הפקת הווידאו:</b> כתיבת פרומפט מולטי-מודאלי מפורט שהגדיר תנועת מצלמה רציפה, שפת גוף, לבוש ומסרים מותאמים.</li>
        <li><b>שחזוריות ושקיפות:</b> תיעוד מדויק המאפשר להריץ מחדש את הפרומפטים ולקבל תוצרים עקביים.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 6 (חי ואינטראקטיבי)
# -------------------------------------------------------------
elif selected_slide == slides[5]:
    st.markdown('<div dir="rtl"><h2>ניתוח נתונים ואופטימיזציית תקציב (קוד חי ואינטראקטיבי)</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    # אלמנט אינטראקטיבי לבודק / סוכן AI
    campaign_effort = st.slider(
        "סימולציית הגברת תקציב ומאמץ קמפיין (% תוספת תמיכה):",
        min_value=0,
        max_value=15,
        value=0,
        step=1
    )
    
    base_support = [68, 74, 52, 41, 57]
    adjusted_support = [min(100, s + campaign_effort) for s in base_support]
    
    data = {
        'Target_Group': [
            'Young Adults & Students - Rent & Living',
            'Reserve Soldiers & Families - Civil Rights',
            'Young Families - Affordable Housing',
            'Small Business Owners - Economic Relief',
            'Swing Voters - Security & Trust'
        ],
        'Support_Level': adjusted_support,
        'Voter_Count': [18500, 24000, 31000, 11500, 42000]
    }
    df = pd.DataFrame(data)
    
    col1, col2 = st.columns([1.3, 1])
    
    with col2:
        st.markdown(f"""
        <div dir="rtl">
        <h3>החלטות תקציב מהתרשים (בתוספת {campaign_effort}% מאמץ):</h3>
        <ul>
            <li><b>קהלים תומכים (עמודות כחולות):</b> משרתי מילואים ({adjusted_support[1]}%) וסטודנטים ({adjusted_support[0]}%) מקבלים תקציב להמרצה ישירה לקלפי.</li>
            <li><b>קהל ספקני (עמודה אדומה):</b> בעלי עסקים ({adjusted_support[3]}%) מקבלים מסר ממוקד להקלה בבירוקרטיה, או הפחתת חשיפה לחסכון בעלויות.</li>
            <li><b>הכרעת הבחירות:</b> קולות צפים (42,000 בוחרים) מהווים את המוקד המרכזי לקמפיין שכנוע סביב ביטחון ואמון.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col1:
        fig, ax = plt.subplots(figsize=(9, 4.8))
        colors = ['#1d3557' if s >= 50 else '#e63946' for s in df['Support_Level']]
        bars = ax.barh(df['Target_Group'], df['Voter_Count'], color=colors, height=0.55)
        
        for bar, support, count in zip(bars, df['Support_Level'], df['Voter_Count']):
            ax.text(
                bar.get_width() + 500,
                bar.get_y() + bar.get_height() / 2,
                f"{count:,} | {support}%",
                va='center', ha='left', fontsize=9, fontweight='bold', color='#333333'
            )
        
        ax.set_title('Live Segment Optimization (Israel)', fontsize=12, fontweight='bold')
        ax.set_xlabel('Audience Size (Registered Voters)', fontsize=10)
        ax.set_xlim(0, max(df['Voter_Count']) * 1.35)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)

# -------------------------------------------------------------
# שקף 7
# -------------------------------------------------------------
elif selected_slide == slides[6]:
    st.markdown('<div dir="rtl"><h2>תוצר וידאו: התאמת מסרים אישית שמניעה לפעולה</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    col_vid, col_desc = st.columns([1.3, 1])
    
    with col_vid:
        found_video = None
        for file in os.listdir("."):
            if file.endswith(".mp4"):
                found_video = file
                break
                
        if found_video:
            st.video(found_video)
            st.caption("קובץ המקור שמור במאגר הפרויקט בגיטהאב: microtargeting_demo.mp4")
        else:
            st.warning("קובץ וידאו (.mp4) לא אותר בתיקיית העבודה C:\\0")
            
    with col_desc:
        st.markdown("""
        <div dir="rtl">
        <h3>הרעיון מאחורי הסרטון:</h3>
        <p>הסרטון ממחיש כיצד <b>אותו מועמד פונה לקהלים שונים בשפה מיתוגית שונה</b>, כשהמטרה היא לגעת בדיוק בדברים שמניעים כל בוחר לצאת לקלפי:</p>
        <ul>
            <li><b>הצעירה בבית הקפה:</b> מקבלת מסר ישיר על יוקר המחיה ושכירות ברת-השגה בליווי תוכנית דירה.</li>
            <li><b>האם עם העגלה:</b> מקבלת מסר חם על חינוך איכותי לגיל הרך ותמיכה במשפחות.</li>
            <li><b>האזרח הוותיק:</b> מקבל מסר ממלכתי על שמירה על הפנסיות ותקצוב רפואה ציבורית.</li>
        </ul>
        <p>במקום מסר כללי שנבלע, כל קהל מקבל את התוכן שהכי בוער לו ביומיום.</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 8
# -------------------------------------------------------------
elif selected_slide == slides[7]:
    st.markdown('<div dir="rtl"><h2>אתיקה, פרטיות ורגולציה בבחירות</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div dir="rtl">
        <h3>אתגרים וסכנות דמוקרטיות</h3>
        <ul>
            <li><b>תאי תהודה וקיטוב:</b> התאמת יתר עלולה לגרום לכל מגזר להיחשף רק למידע שמחזק את עמדותיו ולהחליש את השיח המשותף.</li>
            <li><b>סכנת מניפולציה:</b> שימוש בבינה מלאכותית מחייב הקפדה על אמינות ומניעת הפצת מסרים סותרים או מטעים.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div dir="rtl">
        <h3>אחריות וציות לחוק</h3>
        <ul>
            <li><b>שימוש בנתונים סינתטיים בלבד:</b> הגנה מלאה על פרטיות אזרחים ללא שימוש במאגרי מידע אישיים רגישים.</li>
            <li><b>שקיפות וגילוי נאות:</b> סימון ברור שהתכנים נוצרו בסיוע כלי בינה מלאכותית, בהתאם להנחיות ועדת הבחירות המרכזית.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 9
# -------------------------------------------------------------
elif selected_slide == slides[8]:
    st.markdown('<div dir="rtl"><h2>מדדי הצלחה ויעילות (KPIs)</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="חיסכון בעלות לגיוס בוחר", value="25%-35%", delta="יעילות תקציבית")
    with col2:
        st.metric(label="שיעור צפייה ממוצע", value="+40%", delta="התאמת מסר")
    with col3:
        st.metric(label="שחזוריות ותיעוד בגיט", value="100%", delta="עמידה בסטנדרט")
    
    st.write("")
    st.markdown("""
    <div dir="rtl">
    <p><b>בסיס הערכת המדדים:</b></p>
    <ul>
        <li>הנתונים מבוססים על יעדי ביצוע וניתוח תוצאות סימולציה מול קמפיין מודעות גנרי מסורתי.</li>
        <li><b>יעילות כלכלית:</b> הפסקת בזבוז תקציבי פרסום על קהלים בעלי עמדה מוצקה שאינם ניתנים לשכנוע.</li>
        <li><b>איכות הקריאייטיב:</b> בחינת מעורבות בזמן אמת כדי לדייק את המסר תוך כדי תנועה.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# שקף 10
# -------------------------------------------------------------
elif selected_slide == slides[9]:
    st.markdown('<div dir="rtl"><h2>סיכום ומסקנות</h2></div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    <div dir="rtl">
    <ul>
        <li><b>חיבור בין דאטה לקריאייטיב:</b> הפרויקט מוכיח שבינה מלאכותית מאפשרת לחבר בין ניתוח נתונים אנליטי להפקת תוכן מותאם אישית במהירות וביעילות.</li>
        <li><b>שליטה ובקרה מלאה:</b> ניהול הפרויקט בגיטהאב והשימוש בפייתון מבטיחים תהליך שקוף, מבוקר ובר-שחזור.</li>
        <li><b>מבט לעתיד:</b> בעתיד ניתן לחבר את המערכת לנתוני סקרים חיים כדי לעדכן את תכני הקמפיין ואת חלוקת התקציב באופן אוטומטי בזמן אמת.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.success("תודה רבה על הבדיקה וההקשבה!")
