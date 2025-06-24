import streamlit as st
import sqlite3
import base64
from PIL import Image
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

# --- Load and encode logos ---
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load assets
logo_icon = Image.open("images/little_logo.png")
dark_logo = encode_image("images/dark_logo.png")
light_logo = encode_image("images/light_logo.png")

# --- Set page config ---
st.set_page_config(
    layout="wide",
    page_title="Naked Innovations - Driving Food System Transformation",
    page_icon=logo_icon
)

def st_normal():
    _, col, _ = st.columns([1, 2, 1])
    return col

# --- Inject Custom CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
            
    :root {{
        --primary-color: #007AFF;
        --secondary-background-color: #F5F5F5;
        --text-color: #0D2B5C;
        --font: "Montserrat", sans-serif;
    }}
    .stButton>button {{
        color: white !important;
        background-color: #007AFF !important;
        border: none !important;
        border-radius: 8px;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: #005FCC !important;
        cursor: pointer;
    }}
    .stButton>button:focus {{
        outline: none !important;
        box-shadow: 0 0 0 0.15rem rgba(0, 122, 255, 0.4) !important;
    }}      
    .stRadio [role="radiogroup"] > label {{
        border: none !important;
        padding: 0.25rem 1rem;
        margin-right: 0.5rem;
        font-weight: 500;
        color: #0D2B5C;
    }}
    .stRadio [role="radiogroup"] > label:hover {{
        background-color: #e6f0ff;
        border-radius: 999px;
        cursor: pointer;
    }}      
    .block-container {{
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100% !important;
    }}
    html, body {{
        font-family: 'Montserrat', sans-serif;
        background-color: #ffffff;
    }}
    .navbar {{
        background-color: #ffffff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0rem 2rem;
        border-bottom: 1px solid #e0e0e0;
        position: sticky;
        top: 0;
        z-index: 1000;
    }}
    .navbar-links a {{
        margin: 0 1rem;
        text-decoration: none;
        color: #0D2B5C;
        font-weight: 500;
    }}
    .hero-tight {{
        padding: 1rem 0 1rem 0;
    }}
    .hero-tight h2 {{
        color: #2495F3;
        font-weight: 700;
        font-size: 2rem;
        margin: 0;
        line-height: 1.3;
        text-transform: uppercase;
        text-align: center;
    }}
    .hero-tight h1 {{
        color: #0D2B5C;
        font-size: 1.75rem;
        font-weight: 700;
        padding-top: 0;
    }}
    .button-primary {{
        background-color: #007AFF;
        color: white !important;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin-top: 1rem;
    }}
    .footer {{
        background-color: #0D2B5C;
        color: white;
        padding: 3rem 2rem;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-top: 5rem;
    }}
    .footer a {{
        color: white;
        text-decoration: none;
        display: block;
        margin: 0.25rem 0;
    }}       
    .touch-box {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 2.5rem 2rem;
        border-radius: 16px;
        border: 2px solid #FECF2F;
        width: 520px;
        color: white;
        font-size: 1.1rem;
        margin-top: 1.5rem;
    }}
    .logo-header {{
        height: 70px;
        object-fit: contain;
    }}
    .logo-footer {{
        height: 100px;
        margin-bottom: 1rem;
    }}
    .persona-inline {{
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-top: 0rem;
        flex-wrap: wrap;
    }}
    .persona-label {{
        margin: 0;
        font-size: 1.05rem;
        color: #1C1C1E;
    }}
    .persona-badge {{
        background-color: #007AFF;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1.1rem;
        white-space: nowrap;
    }}
    .persona-badge:hover {{
        transform: scale(1.05);
    }}    
    .results-card {{
        background-color: #F9FAFC;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-top: 1rem;
        text-align: justify;
    }}
    .results-card p {{
        font-size: 1.25rem;
        line-height: 1.6;
        color: #1C1C1E;
        margin-bottom: 1rem;
    }}
    .footer-links {{
        display: flex;
        gap: 4rem;
        margin-top: 1rem;
    }}
    .footer-links div {{
        display: flex;
        flex-direction: column;
    }}
    .footer-links strong {{
        color: white;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }}
    .footer-heading {{
        color: white;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 0.75rem;
    }}
    .footer-content {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        flex-wrap: wrap;
        gap: 3rem;
        padding-top: 2rem;
    }}
    .footer-left {{
        max-width: 500px;
    }}
    .footer-right {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 1.5rem;
        min-width: 280px;
    }}
    .newsletter-box {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 2rem;
        border: 1px solid #ffffff55;
        border-radius: 12px;
        background-color: transparent;
        color: white;
        width: 520px;
        font-weight: 700;
        font-size: 1.1rem;
    }}      
    .newsletter-box a.button-primary {{
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: 700;
    }}
    @media screen and (max-width: 768px) {{
        .navbar {{
            flex-direction: column;
            align-items: flex-start;
        }}
        .navbar-links {{
            display: flex;
            flex-wrap: wrap;
            margin-top: 1rem;
        }}
        .navbar-links a {{
            margin: 0.5rem 0.5rem 0 0;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- Render Header ---
st.markdown(f"""
    <div class="navbar">
        <div>
            <img src="data:image/png;base64,{dark_logo}" height="40" class="logo-header">
        </div>
        <div class="navbar-links">
            <a href="https://www.nakedinnovations.eu/">Home</a>
            <a href="https://www.nakedinnovations.eu/about">About</a>
            <a href="https://www.nakedinnovations.eu/services">Services</a>
            <a href="https://www.nakedinnovations.eu/blog">Blog</a>
            <a href="https://www.nakedinnovations.eu/blog/spotlight-naked-innovations-success-stories">Case Studies</a>
            <a href="https://www.nakedinnovations.eu/alt-protein-club">Alt Protein Club</a>
            <a class="button-primary" href="https://www.nakedinnovations.eu/contact">Let's Connect</a>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- DB setup ---
conn = sqlite3.connect('innovation_survey_responses.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS innovation_survey_responses (
    email TEXT PRIMARY KEY,
    company_name TEXT,
    industry TEXT,
    q1k TEXT, q2k TEXT, q3k TEXT, q4k TEXT, q5k INTEGER,
    q1m TEXT, q2m TEXT, q3m TEXT, q4m TEXT, q5m INTEGER,
    q1p TEXT, q2p TEXT, q3p TEXT, q4p TEXT, q5p INTEGER,
    total_score INTEGER,
    knowledge_score INTEGER,
    mindset_score INTEGER,  
    processes_score INTEGER,
    stage TEXT,
    persona TEXT
)
''')
conn.commit()

# --- Survey ---
def survey():
    st.markdown("""<div class="hero-tight"><h2>INNOVATION ECOSYSTEM READINESS</h2></div>""", unsafe_allow_html=True)

    if "section" not in st.session_state:
        st.session_state.section = "info"
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "answers" not in st.session_state:
        st.session_state.answers = []

    if st.session_state.section == "info":
        with st_normal():
            with st.container(border=True):
                st.markdown("""<div class="hero-tight"><h1>Tell us about yourself</h1></div>""", unsafe_allow_html=True)
                email = st.text_input("Enter your email address")
                company_name = st.text_input("Enter your company name")
                industry = st.selectbox("Select your industry", (
                    'Product Manufacturers',
                    'Technology & Solutions Providers',
                    'Distributors & Retailers',
                    'Primary Producers & Raw Materials',
                    'Innovation & Support Ecosystems'
                ))
                if st.button("Next"):
                    if email and company_name:
                        st.session_state.email = email
                        st.session_state.company_name = company_name
                        st.session_state.industry = industry
                        st.session_state.section = "knowledge"
                        st.session_state.step = 0
                        st.rerun()
                    else:
                        st.warning("Please fill in both your email and company name.")

    def ask_radio(label, key):
        return st.radio(label, ('1', '2', '3', '4', '5'), horizontal=True, key=key)

   # Questions for each section
    knowledge_questions = [
        "I understand how emerging technologies and methods can be leveraged to drive innovation in our core operations.",
        "I regularly monitor relevant market, regulatory and industry trends to inform our strategic direction.",
        "I am familiar with best practices for collaborating with external partners (e.g., suppliers, startups, research institutions).",
        "I know how to use data and performance metrics to guide continuous improvement and new-product development.",
    ]
    mindset_questions = [
        "Our leadership actively champions the adoption of new technologies, methods or business models.",
        "Employees at all levels are encouraged to propose ideas and experiment with new approaches.",
        "We are willing to invest resources in pilot projects even if the returns may take time to materialize.",
        "We collaborate regularly with external experts—clients, partners or research organizations—to co-create solutions.",
    ]
    process_questions = [
        "We have a clear, formal process for capturing, evaluating and prioritizing new ideas.",
        "Our teams rapidly incorporate feedback from stakeholders (e.g., customers, suppliers, quality control) into each iteration.",
        "We move from concept approval to small-scale prototype (or pilot) within a specified short timeframe (e.g., two weeks).",
        "We regularly host structured ideation events (hackathons, sprints or workshops) to generate and refine concepts."
    ]

    if st.session_state.section == "knowledge":
        with st_normal():
            with st.container(border=True):
                st.markdown("""<div class="hero-tight"><h1>Knowledge</h1></div>""", unsafe_allow_html=True)
                if st.session_state.step < len(knowledge_questions):
                    q = knowledge_questions[st.session_state.step]
                    ans = ask_radio(q, f"qk{st.session_state.step}")
                    if st.button("Next"):
                        st.session_state.answers.append(ans)
                        st.session_state.step += 1
                        st.rerun()
                elif st.session_state.step == len(knowledge_questions):
                    q5k = st.number_input("What percentage of your workforce has participated in training or learning programs?", key="qk4")
                    if st.button("Next"):
                        st.session_state.answers.append(q5k)
                        st.session_state.section = "mindset"
                        st.session_state.step = 0
                        st.rerun()

    elif st.session_state.section == "mindset":
        with st_normal():
            with st.container(border=True):
                st.markdown("""<div class="hero-tight"><h1>Mindset</h1></div>""", unsafe_allow_html=True)
                if st.session_state.step < len(mindset_questions):
                    q = mindset_questions[st.session_state.step]
                    ans = ask_radio(q, f"qm{st.session_state.step}")
                    if st.button("Next"):
                        st.session_state.answers.append(ans)
                        st.session_state.step += 1
                        st.rerun()
                elif st.session_state.step == len(mindset_questions):
                    q5m = st.number_input("What percentage of your workforce is in innovation/product development?", key="qm4")
                    if st.button("Next"):
                        st.session_state.answers.append(q5m)
                        st.session_state.section = "processes"
                        st.session_state.step = 0
                        st.rerun()

    elif st.session_state.section == "processes":
        with st_normal():
            with st.container(border=True):
                st.markdown("""<div class="hero-tight"><h1>Processes</h1></div>""", unsafe_allow_html=True)
                if st.session_state.step < len(process_questions):
                    q = process_questions[st.session_state.step]
                    ans = ask_radio(q, f"qp{st.session_state.step}")
                    if st.button("Next"):
                        st.session_state.answers.append(ans)
                        st.session_state.step += 1
                        st.rerun()
                elif st.session_state.step == len(process_questions):
                    q1p, q2p, q3p = map(int, st.session_state.answers[-3:])
                    lowest_q = min(q1p, q2p, q3p)
                    if lowest_q == q1p:
                        q4p = ask_radio('We host demo days or innovation challenges to help teams develop and launch new ventures.', "qp3")
                    elif lowest_q == q2p:
                        q4p = ask_radio('We use a structured system to capture and implement ideas from ecosystem participants.', "qp3")
                    else:
                        q4p = ask_radio('We have a defined pathway for scaling successful pilots into funded programs or spin-outs.', "qp3")

                    if st.button("Next"):
                        st.session_state.answers.append(q4p)
                        st.session_state.step += 1
                        st.rerun()
                elif st.session_state.step == len(process_questions) + 1:
                    q5p = st.number_input("On average, how many iterations before full implementation?", key="qp4")
                    
                    if st.button("View my results"):
                        st.session_state.answers.append(q5p)

                        if len(st.session_state.answers) == 15:
                            [q1k, q2k, q3k, q4k, q5k,
                            q1m, q2m, q3m, q4m, q5m,
                            q1p, q2p, q3p, q4p, q5p] = st.session_state.answers
                        else:
                            st.error("Unexpected number of answers collected. Please restart the survey.")
                            st.stop()

                        # Unpack
                        [q1k, q2k, q3k, q4k, q5k,
                        q1m, q2m, q3m, q4m, q5m,
                        q1p, q2p, q3p, q4p, q5p] = st.session_state.answers

                        # Scoring
                        knowledge_score = sum(map(int, [q1k, q2k, q3k, q4k]))
                        mindset_score = sum(map(int, [q1m, q2m, q3m, q4m]))
                        processes_score = sum(map(int, [q1p, q2p, q3p, q4p]))
                        total_score = knowledge_score + mindset_score + processes_score

                        if (total_score / 60) * 100 < 51:
                            stage = 'Explorer'
                        elif (total_score / 60) * 100 < 71:
                            stage = 'Builder'
                        elif (total_score / 60) * 100 < 86:
                            stage = 'Connector'
                        else:
                            stage = 'Catalyst'

                        if knowledge_score > mindset_score and knowledge_score > processes_score:
                            persona = 'Architect' if mindset_score > processes_score else 'Engineer'
                            if abs(mindset_score - processes_score) < 2:
                                persona = 'Philosopher'
                        elif mindset_score > knowledge_score and mindset_score > processes_score:
                            persona = 'Campaigner' if knowledge_score > processes_score else 'Believer'
                            if abs(knowledge_score - processes_score) < 2:
                                persona = 'Dreamer'
                        elif processes_score > knowledge_score and processes_score > mindset_score:
                            persona = 'Driver' if knowledge_score > mindset_score else 'Operator'
                            if abs(knowledge_score - mindset_score) < 2:
                                persona = 'Enabler'
                        else:
                            persona = 'Holistic Innovator'

                        # Save
                        cursor.execute('''
                            INSERT OR REPLACE INTO innovation_survey_responses (
                                email, company_name, industry,
                                q1k, q2k, q3k, q4k, q5k,
                                q1m, q2m, q3m, q4m, q5m,
                                q1p, q2p, q3p, q4p, q5p,
                                total_score, knowledge_score, mindset_score, processes_score,
                                stage, persona
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (st.session_state.email, st.session_state.company_name, st.session_state.industry, q1k, q2k, q3k, q4k, q5k,
                            q1m, q2m, q3m, q4m, q5m, q1p, q2p, q3p, q4p, q5p,
                            total_score, knowledge_score, mindset_score, processes_score,
                            stage, persona))
                        conn.commit()
                        # st.session_state.success_message = f"You are a **{persona}** in the **{stage}** stage!"
                        st.session_state.page = 'results'
                        st.rerun()

# --- Results ---
def results():

    tab1, tab2 = st.tabs(['Ecosystem Readiness', 'Persona'])
    email = st.session_state.get('email', None)
    if not email:
        st.error("No email found. Please complete the survey first.")
        st.button('Back to Survey', on_click=lambda: st.session_state.update(page='survey'))
        return

    cursor.execute('''
    SELECT stage, persona, knowledge_score, mindset_score, processes_score FROM innovation_survey_responses WHERE email = ?
    ''', (email,))
    result = cursor.fetchone()
    if result:
        stage, persona, knowledge_score, mindset_score, processes_score = result
    else:
        st.error("No results found for this email.")
        return
        
    with tab1:
        st.markdown("""<div class="hero-tight"><h1>Ecosystem Readiness</h1></div>""", unsafe_allow_html=True)
        st.write(f'You are in the **{stage}** stage of the innovation ecosystem! Check out your persona to better understand your role in the innovation landscape.')

        share_link = "http://localhost:8501" 
        #st.text_input("Share this link:", value=share_link, disabled=True,label_visibility="collapsed")

        st.markdown(f"""
        <div style="max-width: 650px;">
            <pre><code>{share_link}</code></pre>
        </div>
        """, unsafe_allow_html=True)

        st.write("Copy the link above and share it with someone else to invite them to take the survey.")


    with tab2:
        st.markdown("""<div class="hero-tight"><h1>Persona results</h1></div>""", unsafe_allow_html=True)

        persona_text = None
        if persona == 'Architect':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are an</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text = '''Your company brings a compelling strategic vision, grounded in deep market knowledge and technological insight. 
                     You are seen as the idea generator—your awareness of innovation trends and emerging tools positions you to inspire not just internally, but across your ecosystem. 
                     While executional structures may still be maturing, your influence is clear: teams rally behind your vision, eager to explore what's possible. 
                     As you continue to strengthen internal alignment and cross-functional collaboration, you're set to translate strategic foresight into bold, ecosystem-driven innovations that shape your industry's future.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Engineer':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are an</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text ='''You excel at turning ideas into reality through strong internal systems and a structured approach to innovation. 
                     Your organization knows how to get things done—your ability to manage innovation workflows, test rapidly, and scale efficiently makes you a reliable partner for collaborative ventures. 
                     Your deep knowledge enables you to build smart, scalable solutions, while your operational strength ensures consistency. 
                     To take your impact to the next level, fostering a more visionary mindset within leadership can unlock greater transformative potential and help spark game-changing innovation from within.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Philosopher':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are a</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text = '''Your company reflects a rare balance of expertise, openness, and operational maturity. 
                     You blend strategic knowledge with a willingness to explore and iterate, supported by structures that enable steady progress. 
                     Teams collaborate with purpose, ideas are evaluated thoughtfully, and your organization moves with intention. 
                     This harmony of knowledge, mindset, and execution readiness gives you a strong foundation to lead innovation that is both impactful and enduring. 
                     With continued focus, you're poised not just to innovate, but to shape a sustainable culture of learning and shared value across your industry network.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        if persona == 'Campaigner':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are a</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text = '''Your company demonstrates a strong commitment to innovation through leadership that inspires and motivates others. 
                     There's a clear drive to integrate cutting-edge ideas and solutions into the business, with a strong emphasis on learning and improvement. 
                     Your organization is constantly exploring new ways to elevate customer experiences and operational efficiency, while also leveraging external expertise. 
                     This approach positions you as a key influencer in your sector, driving meaningful change and setting the standard for others to follow. 
                     To build on this influence, optimizing internal processes to enable faster innovation could help you stay ahead in an increasingly competitive market.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Believer':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are a</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text ='''Your company is highly adaptable, with leadership that is open to innovation and a focus on continuous improvement. 
                     Employees are encouraged to experiment and contribute to evolving processes, and there's a willingness to take calculated risks. 
                     This puts you in a strong position to lead industry transformation. 
                     To further strengthen your position, refining the integration of new ideas and technologies could allow for faster and more impactful change, ensuring that your current approach to innovation continues to evolve and drive industry leadership.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Dreamer':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are a</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text ='''Your company has a strong culture of collaboration and values innovation. 
                     There's a thoughtful and steady approach to adopting new technologies and processes, which helps create a stable environment for growth. 
                     Your alignment between company values and strategic direction supports sustainable, long-term change. 
                     By building on your existing internal culture, seeking external perspectives could provide fresh insights that complement your approach and accelerate the pace of change, helping you stay competitive in a rapidly evolving market.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        if persona == 'Driver':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are a</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text = '''You have built a strong foundation of processes that allow you to move quickly from idea to action. Your strength lies in execution—getting things done efficiently and at scale. 
                     This makes you a valuable partner in ecosystem collaborations, especially where speed and structure are crucial. 
                     To elevate your innovation capacity further, investing in building internal knowledge and capability around emerging practices and fostering leadership vision will ensure your actions are guided by strategic foresight, not just efficiency.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Operator':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are an</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text = '''Your company has clearly established operational capabilities and leadership support that enable consistent and scalable innovation. 
                     You're good at turning ideas into real results, and your internal alignment ensures that priorities are well-executed. 
                     With this strong foundation, focusing more on developing and applying new knowledge—especially in emerging technologies and market trends—can help your organization anticipate shifts before they happen and lead the innovation curve rather than just follow it.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Enabler':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are an</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text ='''You are in a strong position to translate innovative ideas into action, thanks to your balance of collaborative leadership and agile operations. 
                     Your teams work well together and are empowered by a culture that values execution and adaptability. 
                     This allows you to enable others—both inside and outside your organization—to succeed in innovation. 
                     To deepen your strategic role, focusing on knowledge development and external trend awareness can enhance your influence and help drive more forward-thinking innovation agendas.'''
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)
        elif persona == 'Holistic Innovator':
            st.markdown(f"""<div class="persona-inline"><p class="persona-label">Based on your innovation profile, you are a</p><span class="persona-badge">{persona}</span></div>""", unsafe_allow_html=True)
            persona_text = 'Your organization demonstrates a rare and powerful balance across knowledge, mindset, and processes. You combine deep expertise, visionary leadership, and operational agility to lead innovation comprehensively. This balance allows you to co-create impactful solutions, scale them efficiently, and inspire your broader ecosystem. You are well-positioned to act as a role model for innovation excellence. To maintain this edge, continue refining your innovation strategy and exploring new collaboration models that push boundaries while reinforcing your strengths.'
            st.markdown(f'<div class="results-card">{persona_text}</div>', unsafe_allow_html=True)

        # --- PDF Download Button ---
        if persona_text:
            pdf_buffer = io.BytesIO()
            c = canvas.Canvas(pdf_buffer, pagesize=A4)
            width, height = A4
            # Draw background color
            c.setFillColorRGB(1, 1, 1)  # white
            c.rect(0, 0, width, height, fill=1)
            # Draw logo (top left)
            logo_y = height-120
            try:
                c.drawImage("images/dark_logo.png", 40, logo_y, width=120, preserveAspectRatio=True, mask='auto')
            except Exception:
                pass
            # Add vertical space below logo before title
            title_y = logo_y - 15  # further reduced gap (was 35)
            # Centered, larger, bolder Title
            c.setFont("Helvetica-Bold", 26)
            c.setFillColorRGB(0, 0.48, 1)  # #007AFF
            title = "Innovation Ecosystem Readiness Report"
            title_width = c.stringWidth(title, "Helvetica-Bold", 26)
            c.drawString((width-title_width)/2, title_y, title)
            # User info section
            info_y = title_y - 50
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(colors.HexColor("#0D2B5C"))
            c.drawString(40, info_y, "Name:")
            c.setFont("Helvetica", 11.5)
            c.drawString(110, info_y, f"{st.session_state.get('company_name','')}")
            c.setFont("Helvetica-Bold", 13)
            c.drawString(40, info_y-22, "Email:")
            c.setFont("Helvetica", 11.5)
            c.drawString(110, info_y-22, f"{email}")
            # Persona label and value larger and bolder
            c.setFont("Helvetica-Bold", 17)
            c.setFillColor(colors.HexColor("#007AFF"))
            persona_label = f"Persona: {persona}"
            c.drawString(40, info_y-50, persona_label)
            # Persona description section
            desc_header_y = info_y-74
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(colors.HexColor("#0D2B5C"))
            c.drawString(40, desc_header_y, "Persona Description")
            c.setFont("Helvetica", 11)
            c.setFillColor(colors.HexColor("#1C1C1E"))
            from reportlab.lib.utils import simpleSplit
            desc_lines = []
            for para in persona_text.split("\n"):
                desc_lines.extend(simpleSplit(para.strip(), "Helvetica", 11, width-80))
            text_obj = c.beginText(40, desc_header_y-18)
            for line in desc_lines:
                text_obj.textLine(line)
            c.drawText(text_obj)
            # Divider line
            divider_y = desc_header_y-18-len(desc_lines)*13-8  # reduce bottom padding after description
            c.setStrokeColor(colors.HexColor("#E0E0E0"))
            c.setLineWidth(1)
            c.line(40, divider_y, width-40, divider_y)
            # 'Your Scores' header
            bars_header_y = divider_y-30  # add ~20px space above 'Your Scores'
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(colors.HexColor("#007AFF"))
            c.drawString(40, bars_header_y, "Your Scores")
            # Score bars
            bar_x = 40
            bar_y = bars_header_y-52  # add ~12px space below 'Your Scores' before first bar
            bar_width = width-160
            bar_height = 18
            bar_gap = 44  # more space between bars
            # Determine which score is highest for coloring
            scores = [knowledge_score, mindset_score, processes_score]
            max_idx = scores.index(max(scores))
            bar_colors = [colors.HexColor("#2495F3"), colors.HexColor("#2495F3"), colors.HexColor("#2495F3")]
            bar_colors[max_idx] = colors.HexColor("#FECF2F")  # yellow for highest
            categories = [
                ("Knowledge", knowledge_score, bar_colors[0]),
                ("Mindset", mindset_score, bar_colors[1]),
                ("Processes", processes_score, bar_colors[2]),
            ]
            max_score = 20
            c.setFont("Helvetica-Bold", 12)
            label_x = bar_x
            bar_start_x = bar_x+70  # reduce horizontal space between label and bar
            for idx, (label, score, color) in enumerate(categories):
                percent = int((score/max_score)*100)
                # Vertically center label with bar: shift baseline down by 6px
                c.setFillColor(colors.HexColor("#0D2B5C"))
                c.drawString(label_x, bar_y+bar_height-2-6, label)
                # Bar background
                c.setFillColor(colors.HexColor("#F5F5F5"))
                c.roundRect(bar_start_x, bar_y, bar_width, bar_height, 8, fill=1, stroke=0)
                # Bar fill
                c.setFillColor(color)
                c.roundRect(bar_start_x, bar_y, bar_width*(score/max_score), bar_height, 8, fill=1, stroke=0)
                # Percentage (centered in bar if space, else to right)
                percent_str = f"{percent}%"
                percent_width = c.stringWidth(percent_str, "Helvetica-Bold", 12)
                bar_fill_width = bar_width*(score/max_score)
                percent_x = bar_start_x + (bar_fill_width-percent_width)/2 if bar_fill_width > percent_width+10 else bar_start_x+bar_width+10
                percent_color = colors.white if bar_fill_width > percent_width+30 else colors.HexColor("#0D2B5C")
                c.setFillColor(percent_color)
                c.drawString(percent_x, bar_y+4, percent_str)
                # For last bar, use a smaller gap to divider to match previous section spacing
                if idx < len(categories)-1:
                    bar_y -= (bar_height + bar_gap - 12)
                else:
                    bar_y -= (bar_height + 14)  # set gap to ~32px (18+14)
            # Divider above Next Steps section
            next_divider_y = bar_y  # set divider exactly 32px below last bar
            c.setStrokeColor(colors.HexColor("#E0E0E0"))
            c.setLineWidth(1)
            c.line(40, next_divider_y, width-40, next_divider_y)
            # Next Steps section
            next_steps_y = next_divider_y-20
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(colors.HexColor("#007AFF"))
            c.drawString(40, next_steps_y, "Next Steps")
            c.setFont("Helvetica", 12)
            c.setFillColor(colors.HexColor("#1C1C1E"))
            c.drawString(40, next_steps_y-18, "Next steps here")
            # Footer tagline
            c.setFont("Helvetica-Oblique", 10)
            c.setFillColor(colors.HexColor("#A0A0A0"))
            c.drawString(40, 32, "Naked Innovations | Driving Food System Transformation")
            # Watermark logo (bottom right, faded)
            try:
                c.saveState()
                c.translate(width-160, 20)
                c.setFillAlpha(0.5)
                c.drawImage("images/dark_logo.png", 0, 0, width=120, preserveAspectRatio=True, mask='auto')
                c.restoreState()
            except Exception:
                pass
            c.showPage()
            c.save()
            pdf_buffer.seek(0)
            # Custom styled download button
            st.markdown(f"""
                <style>
                [data-testid="stDownloadButton"] button[aria-label="Download Persona PDF"] {{
                    background-color: #007AFF !important;
                    color: white !important;
                    border: none !important;
                    border-radius: 12px !important;
                    padding: 0.75rem 2rem !important;
                    font-family: 'Montserrat', sans-serif !important;
                    font-size: 1.1rem !important;
                    font-weight: 600 !important;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                    transition: background 0.2s;
                }}
                [data-testid="stDownloadButton"] button[aria-label="Download Persona PDF"]:hover {{
                    background-color: #005FCC !important;
                }}
                </style>
            """, unsafe_allow_html=True)
            st.download_button(
                label="Download Persona PDF",
                data=pdf_buffer,
                file_name="Naked Innovation Persona Report.pdf",
                mime="application/pdf",
                key="persona_pdf_dl",
                help="Download your personalized persona report as a PDF."
            )

# --- Page Routing ---

if 'page' not in st.session_state:
    st.session_state['page'] = 'survey'

if st.session_state['page'] == 'survey':
    survey()
elif st.session_state['page'] == 'results':
    results()



# --- Render Footer ---
st.markdown(f"""<div class="footer">
        <div>
            <div class="footer-left">
            <img src="data:image/png;base64,{light_logo}" height="40" class='logo-footer'><br><br>
            <p class="footer-heading">Pages</p>
            <div class="footer-links">
                <div>
                    <a href="https://www.nakedinnovations.eu/">Home</a>
                    <a href="https://www.nakedinnovations.eu/about">About</a>
                    <a href="https://www.nakedinnovations.eu/services">Services</a>
                </div>
                <div>
                    <a href="https://www.nakedinnovations.eu/blog">Blog</a>
                    <a href="https://www.nakedinnovations.eu/blog/spotlight-naked-innovations-success-stories">Case Studies</a>
                    <a href="https://www.nakedinnovations.eu/contact">Contact</a>
                </div>
            </div>
        </div>
        </div>
        <div>
            <div class="newsletter-box">
                <span>Sign up to receive our newsletter</span>
                <a class="button-primary" href="https://www.nakedinnovations.eu/sign-up-now">Sign Up</a>
            </div>
            <div class="touch-box">
                <div>
                    <div style="font-weight: 700; font-size: 1.3rem;">Don't be a stranger :)</div>
                    <div style="color: #cbd5e1; font-weight: 500;">info@nakedinnovations.eu</div>
                </div>
                <a class="button-primary" href="mailto:info@nakedinnovations.eu" style="padding: 0.6rem 1.5rem; font-weight: 700;">Get in Touch</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
