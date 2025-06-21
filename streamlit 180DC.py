import streamlit as st
import sqlite3

conn=sqlite3.connect('innovation_survey_responses.db')
cursor=conn.cursor()

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

def survey():
    st.title('Innovation Ecosystem Readiness')

    email = st.text_input('Enter your email address')
    company_name = st.text_input('Enter your company name')
    industry = st.selectbox('Select your industry', (
        'Product Manufacturers', 
        'Technology & Solutions Providers', 
        'Distributors & Retailers', 
        'Primary Producers & Raw Materials', 
        'Innovation & Support Ecosystems'
    ))

    st.empty()

    st.subheader('Knowledge')
    if industry == 'Product Manufacturers':
        q1k=st.radio('I understand how advanced manufacturing technologies (e.g., automation, IoT, digital twins) can be leveraged to innovate our production processes.', ('1', '2', '3', '4', '5'))
        q2k=st.radio('I stay updated on evolving safety, sustainability, and quality standards relevant to our industry.', ('1', '2', '3', '4', '5'))
        q3k=st.radio('I am familiar with best practices in collaborating with suppliers, technology providers, or R&D partners for new product development.', ('1', '2', '3', '4', '5'))
        q4k=st.radio('I have a good understanding of how data and performance metrics can inform continuous production improvements.', ('1', '2', '3', '4', '5'))
        q5k=st.number_input('What percentage of your workforce has participated in training, workshops, or learning programs aimed at updating their innovation-related knowledge in the past 12 months?')
    
    elif industry == 'Technology & Solutions Providers':
        q1k=st.radio('I understand how open innovation models (e.g., developer communities, APIs, tech incubators) can support product development.', ('1', '2', '3', '4', '5'))
        q2k=st.radio('I stay up to date with the latest trends in emerging technologies (e.g., AI, blockchain, cybersecurity) relevant to our solutions', ('1', '2', '3', '4', '5'))
        q3k=st.radio('I am proficient in structuring or participating in co-innovation projects with external partners or clients.', ('1', '2', '3', '4', '5'))
        q4k=st.radio('I know how to manage knowledge flow and intellectual property when collaborating externally.', ('1', '2', '3', '4', '5'))
        q5k=st.number_input('What percentage of your workforce has participated in training, workshops, or learning programs aimed at updating their innovation-related knowledge in the past 12 months?')

    elif industry == 'Distributors & Retailers':
        q1k=st.radio('I understand supply chain innovation practices (e.g., real-time tracking, demand forecasting) that enhance efficiency and collaboration.', ('1', '2', '3', '4', '5'))
        q2k=st.radio('I am familiar with digital tools (e.g., CRM, ERP, e-commerce analytics) that support data-driven decision-making in retail and distribution.', ('1', '2', '3', '4', '5'))
        q3k=st.radio('I track trends in customer behavior, market preferences, and logistics innovations relevant to our business.', ('1', '2', '3', '4', '5'))
        q4k=st.radio('I am aware of how partnerships with vendors or platforms can improve our customer experience and operations.', ('1', '2', '3', '4', '5'))
        q5k=st.number_input('What percentage of your workforce has participated in training, workshops, or learning programs aimed at updating their innovation-related knowledge in the past 12 months?')

    elif industry == 'Primary Producers & Raw Materials':
        q1k=st.radio('I understand key external collaboration methods relevant to our sector (e.g., joint research, industry-wide initiatives).', ('1', '2', '3', '4', '5'))
        q2k=st.radio('I keep track of market and regulatory trends that affect resource management and sustainability.', ('1', '2', '3', '4', '5'))
        q3k=st.radio('I am knowledgeable about technologies (e.g., precision farming, drones, sensors) that improve efficiency and sustainability.', ('1', '2', '3', '4', '5'))
        q4k=st.radio('I am familiar with best practices for managing the environmental and social aspects of innovation partnerships.', ('1', '2', '3', '4', '5'))
        q5k=st.number_input('What percentage of your workforce has participated in training, workshops, or learning programs aimed at updating their innovation-related knowledge in the past 12 months?')

    elif industry == 'Innovation & Support Ecosystems':
        q1k=st.radio('I understand co-innovation frameworks (e.g., hackathons, collaborative labs, research consortia) used in ecosystem innovation.', ('1', '2', '3', '4', '5'))
        q2k=st.radio('I keep pace with emerging tools (e.g., AI, foresight, innovation analytics) used in innovation and strategy consulting.', ('1', '2', '3', '4', '5'))
        q3k=st.radio('I am experienced in protecting intellectual property and data in multi-stakeholder environments.', ('1', '2', '3', '4', '5'))
        q4k=st.radio('I regularly exchange knowledge with peers in academic, public, and private-sector innovation communities.', ('1', '2', '3', '4', '5'))
        q5k=st.number_input('What percentage of your workforce has participated in training, workshops, or learning programs aimed at updating their innovation-related knowledge in the past 12 months?')

    st.subheader('Mindset')

    if industry == 'Product Manufacturers':
        q1m=st.radio('Leadership in our organization champions the adoption of new technologies or methods to improve production efficiency and product quality.', ('1', '2', '3', '4', '5'))
        q2m=st.radio('Employees are empowered to suggest improvements in production techniques, product design, or sustainability efforts.', ('1', '2', '3', '4', '5'))
        q3m=st.radio('We are open to testing new production concepts or technologies, even if the benefits may take time to realize.', ('1', '2', '3', '4', '5'))
        q4m=st.radio('We actively collaborate with R&D partners, universities, or tech providers to explore new product and process innovations.', ('1', '2', '3', '4', '5'))
        q5m=st.number_input('What percentage of your workforce is dedicated to roles directly involved in innovation or product development?')
    
    elif industry == 'Technology & Solutions Providers':
        q1m=st.radio('Our leadership actively promotes innovation in how we build, deliver, or scale our solutions.', ('1', '2', '3', '4', '5'))
        q2m=st.radio('Team members are encouraged to experiment with new technical ideas, tools, or architectures to improve our offerings.', ('1', '2', '3', '4', '5'))
        q3m=st.radio('We’re willing to invest in experimental technologies, even if their commercial application is still evolving.', ('1', '2', '3', '4', '5'))
        q4m=st.radio('We co-develop or partner with clients, research labs, or startups to push the boundaries of our solutions.', ('1', '2', '3', '4', '5'))
        q5m=st.number_input('What percentage of your workforce is dedicated to roles directly involved in innovation or product development?')

    elif industry == 'Distributors & Retailers':
        q1m=st.radio('Leadership supports trying new technologies or service models to improve supply chain efficiency or customer satisfaction.', ('1', '2', '3', '4', '5'))
        q2m=st.radio('Employees are encouraged to suggest changes in logistics, merchandising, or digital engagement strategies.', ('1', '2', '3', '4', '5'))
        q3m=st.radio('We’re willing to pilot new customer experience tools or operational systems, even without a guaranteed outcome.', ('1', '2', '3', '4', '5'))
        q4m=st.radio('We actively engage with tech vendors, service providers, or research teams to explore improvements in logistics and customer touchpoints.', ('1', '2', '3', '4', '5'))
        q5m=st.number_input('What percentage of your workforce is dedicated to roles directly involved in innovation or product development?')

    elif industry == 'Primary Producers & Raw Materials':
        q1m=st.radio('Our leadership backs innovative approaches to improve yields, efficiency, and sustainability in resource production.', ('1', '2', '3', '4', '5'))
        q2m=st.radio('We welcome ideas from staff on how to optimize harvesting, processing, or environmental impact.', ('1','2','3','4','5'))
        q3m=st.radio('We invest in emerging farming/mining/harvesting technologies with long-term potential.', ('1', '2', '3', '4', '5'))
        q4m=st.radio('We partner with researchers, agri-tech firms, or industry groups to innovate in resource management.', ('1', '2', '3', '4', '5'))
        q5m=st.number_input('What percentage of your workforce is dedicated to roles directly involved in innovation or product development?')

    elif industry == 'Innovation & Support Ecosystems':
        q1m=st.radio('Leadership actively encourages experimentation with new innovation methodologies or collaboration models.', ('1', '2', '3', '4', '5'))
        q2m=st.radio('Team members are supported in developing novel approaches to engage startups, partners, or public/private stakeholders.', ('1', '2', '3', '4', '5'))
        q3m=st.radio('We’re open to piloting new innovation formats (e.g., living labs, venture studios), even with uncertain ROI.', ('1', '2', '3', '4', '5'))
        q4m=st.radio('We co-create with academic, government, or private-sector actors to shape new innovation practices.', ('1', '2', '3', '4', '5'))
        q5m=st.number_input('What percentage of your workforce is dedicated to roles directly involved in innovation or product development?')

    st.subheader('Processes')

    if industry == 'Product Manufacturers':
        q1p=st.radio('Our production lines and pilot plants actively support teams to test new product-processing methods.', ('1', '2', '3', '4', '5'))
        q2p=st.radio('We rapidly incorporate feedback from suppliers and quality teams into our production processes.', ('1', '2', '3', '4', '5'))
        q3p=st.radio('We move from recipe concept to small-batch prototype in under two weeks.', ('1', '2', '3', '4', '5'))
        
        if min(q1p,q2p,q3p) == q1p:
            q4p=st.radio('We run recipe hackathons or pilot-run challenges to help teams develop and launch new products', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q2p:
            q4p=st.radio('We use a shared platform to capture and implement packaging or formulation ideas from suppliers', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q3p:
            q4p=st.radio('We have a clear process for scaling successful pilot batches to full-scale production', ('1', '2', '3', '4', '5'))

        q5p=st.number_input('On average, how many iterations does a project undergo before full implementation?')
    
    elif industry == 'Technology & Solutions Providers':
        q1p=st.radio('Our development sandbox and API environments actively support engineers in testing new integrations.', ('1', '2', '3', '4', '5'))
        q2p=st.radio('We rapidly incorporate client and QA feedback into each sprint cycle.', ('1', '2', '3', '4', '5'))
        q3p=st.radio('We deploy test builds to production‐like environments within days of feature conception.', ('1', '2', '3', '4', '5'))
        
        if min(q1p,q2p,q3p) == q1p:
            q4p=st.radio('We host internal hackathons or code-sprints to help teams develop and launch new modules or integrations.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q2p:
            q4p=st.radio('We use a structured workflow to capture and implement partner-submitted feature requests.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q3p:
            q4p=st.radio('We have a clear pipeline for scaling successful prototypes into fully supported releases.', ('1', '2', '3', '4', '5'))

        q5p=st.number_input('On average, how many iterations does a project undergo before full implementation?')

    elif industry == 'Distributors & Retailers':
        q1p=st.radio('Our logistics hubs and store pilots actively support teams to test new shelf-display or delivery methods.', ('1','2','3','4','5'))
        q2p=st.radio('We rapidly incorporate feedback from store managers and suppliers into our distribution plans.', ('1','2','3','4','5'))
        q3p=st.radio('We pilot new merchandising concepts in select stores within one week.', ('1','2','3','4','5'))
        
        if min(q1p,q2p,q3p) == q1p:
            q4p=st.radio('We organize store-pilot events or pop-ups to help teams develop and launch new retail initiatives.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q2p:
            q4p=st.radio('We use a shared system to capture and act on merchandising ideas from suppliers and store teams.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q3p:
            q4p=st.radio('We have a clear process for rolling out successful store pilots chain-wide.', ('1', '2', '3', '4', '5'))
        
        q5p=st.number_input('On average, how many iterations does a project undergo before full implementation?')

    elif industry == 'Primary Producers & Raw Materials':
        q1p=st.radio('Our test plots and ingredient-trial facilities actively support teams to test new farming or harvesting methods.', ('1','2','3','4','5'))
        q2p=st.radio('We rapidly incorporate feedback from agronomists and buyers into our production cycles.', ('1','2','3','4','5'))
        q3p=st.radio('We move from seed variety selection to on-farm trial within two weeks.', ('1','2','3','4','5'))
        
        if min(q1p,q2p,q3p) == q1p:
            q4p=st.radio('We run field days or demo trials to help teams develop and launch new cultivation practices.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q2p:
            q4p=st.radio('We use a structured workflow to capture and implement ideas from research partners and buyers.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q3p:
            q4p=st.radio('We have a clear process for scaling successful field trials to full-scale farm operations.', ('1', '2', '3', '4', '5'))

        q5p=st.number_input('On average, how many iterations does a project undergo before full implementation?')

    elif industry == 'Innovation & Support Ecosystems':
        q1p=st.radio('Our labs and accelerator spaces actively support stakeholders in testing new innovation concepts.', ('1', '2', '3', '4', '5'))
        q2p=st.radio('We rapidly incorporate feedback from startups and academic partners into program iterations.', ('1', '2', '3', '4', '5'))
        q3p=st.radio('We move from concept workshops to live pilot programs within a month.', ('1', '2', '3', '4', '5'))
        
        if min(q1p,q2p,q3p) == q1p:
            q4p=st.radio('We host demo days or innovation challenges to help teams develop and launch new ventures.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q2p:
            q4p=st.radio('We use a structured system to capture and implement ideas from ecosystem participants.', ('1', '2', '3', '4', '5'))
        elif min(q1p,q2p,q3p) == q3p:
            q4p=st.radio('We have a defined pathway for scaling successful pilots into funded programs or spin-outs.', ('1', '2', '3', '4', '5'))
        
        q5p=st.number_input('On average, how many iterations does a project undergo before full implementation?')

    answers=[q1k,q2k,q3k,q4k,q5k,q1m,q2m,q3m,q4m,q5m,q1p,q2p,q3p,q4p,q5p]

    if st.button('Submit'):
        st.session_state['answers'] = answers
        st.session_state['page'] = 'results'
        st.session_state['email'] = email
        st.session_state['company_name'] = company_name
        st.session_state['industry'] = industry
        if email and company_name:
            knowledge_score = sum(map(int, [q1k, q2k, q3k, q4k]))
            mindset_score = sum(map(int, [q1m, q2m, q3m, q4m]))
            processes_score = sum(map(int, [q1p, q2p, q3p, q4p]))
            total_score = knowledge_score + mindset_score + processes_score

            if (total_score/60)*100<51:
                stage = 'Explorer'
            elif (total_score/60)*100<71:
                stage = 'Builder'
            elif (total_score/60)*100<86:
                stage = 'Connector'
            else:
                stage = 'Catalyst'

            if knowledge_score > mindset_score and knowledge_score > processes_score:
                if mindset_score > processes_score:
                    persona = 'Architect'
                elif processes_score > mindset_score:
                    persona = 'Engineer'
                elif abs(mindset_score-processes_score)<2:
                    persona = 'Philosopher'
            elif mindset_score > knowledge_score and mindset_score > processes_score:
                if knowledge_score > processes_score:
                    persona = 'Campaigner'
                elif processes_score > knowledge_score:
                    persona = 'Believer'
                elif abs(knowledge_score-processes_score)<2:
                    persona = 'Dreamer'
            elif processes_score > knowledge_score and processes_score > mindset_score:
                if knowledge_score > mindset_score:
                    persona = 'Driver'
                elif mindset_score > knowledge_score:
                    persona = 'Operator'
                elif abs(knowledge_score-mindset_score)<2:
                    persona = 'Enabler'
            else:
                persona = 'Holistic Innovator'

            cursor.execute('''
            INSERT OR REPLACE INTO innovation_survey_responses (
                email, company_name, industry, q1k, q2k, q3k, q4k, q5k,
                q1m, q2m, q3m, q4m, q5m, q1p, q2p, q3p, q4p, q5p,
                total_score, knowledge_score, mindset_score, processes_score, stage, persona
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (email, company_name, industry, q1k, q2k, q3k, q4k, q5k, q1m, q2m, q3m, q4m, q5m, q1p, q2p, q3p, q4p, q5p,
                  total_score, knowledge_score, mindset_score, processes_score, stage, persona))
            conn.commit()
            st.success('Thank you for your submission!')
        else:
            st.error('Please fill in all required fields.')

def results():

    tab1, tab2 = st.tabs(['Ecosystem Readiness', 'Persona'])
    email = st.session_state.get('email', None)
    if not email:
        st.error("No email found. Please complete the survey first.")
        st.button('Back to Survey', on_click=lambda: st.session_state.update(page='survey'))
        return

    cursor.execute('''
    SELECT stage, persona FROM innovation_survey_responses WHERE email = ?
    ''', (email,))
    result = cursor.fetchone()

    if result:
        stage, persona = result
    else:
        st.error("No results found for this email.")
        return
        
    with tab1:
        st.write(f'You are in the **{stage}** stage of the innovation ecosystem.')

        share_link = "http://localhost:8501" 
        st.text_input("Share this link:", value=share_link, disabled=True)
        st.write("Copy the link above and share it with someone else to invite them to take the survey.")

    with tab2:
        st.title('Persona Results')
        if persona == 'Architect':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your company brings a compelling strategic vision, grounded in deep market knowledge and technological insight. 
                     You are seen as the idea generator—your awareness of innovation trends and emerging tools positions you to inspire not just internally, but across your ecosystem. 
                     While executional structures may still be maturing, your influence is clear: teams rally behind your vision, eager to explore what’s possible. 
                     As you continue to strengthen internal alignment and cross-functional collaboration, you’re set to translate strategic foresight into bold, ecosystem-driven innovations that shape your industry's future.''')
        elif persona == 'Engineer':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     You excel at turning ideas into reality through strong internal systems and a structured approach to innovation. 
                     Your organization knows how to get things done—your ability to manage innovation workflows, test rapidly, and scale efficiently makes you a reliable partner for collaborative ventures. 
                     Your deep knowledge enables you to build smart, scalable solutions, while your operational strength ensures consistency. 
                     To take your impact to the next level, fostering a more visionary mindset within leadership can unlock greater transformative potential and help spark game-changing innovation from within.''')
        elif persona == 'Philosopher':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your company reflects a rare balance of expertise, openness, and operational maturity. 
                     You blend strategic knowledge with a willingness to explore and iterate, supported by structures that enable steady progress. 
                     Teams collaborate with purpose, ideas are evaluated thoughtfully, and your organization moves with intention. 
                     This harmony of knowledge, mindset, and execution readiness gives you a strong foundation to lead innovation that is both impactful and enduring. 
                     With continued focus, you’re poised not just to innovate, but to shape a sustainable culture of learning and shared value across your industry network.''')
        if persona == 'Campaigner':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your company demonstrates a strong commitment to innovation through leadership that inspires and motivates others. 
                     There's a clear drive to integrate cutting-edge ideas and solutions into the business, with a strong emphasis on learning and improvement. 
                     Your organization is constantly exploring new ways to elevate customer experiences and operational efficiency, while also leveraging external expertise. 
                     This approach positions you as a key influencer in your sector, driving meaningful change and setting the standard for others to follow. 
                     To build on this influence, optimizing internal processes to enable faster innovation could help you stay ahead in an increasingly competitive market.''')
        elif persona == 'Believer':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your company is highly adaptable, with leadership that is open to innovation and a focus on continuous improvement. 
                     Employees are encouraged to experiment and contribute to evolving processes, and there’s a willingness to take calculated risks. 
                     This puts you in a strong position to lead industry transformation. 
                     To further strengthen your position, refining the integration of new ideas and technologies could allow for faster and more impactful change, ensuring that your current approach to innovation continues to evolve and drive industry leadership.''')
        elif persona == 'Dreamer':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your company has a strong culture of collaboration and values innovation. 
                     There's a thoughtful and steady approach to adopting new technologies and processes, which helps create a stable environment for growth. 
                     Your alignment between company values and strategic direction supports sustainable, long-term change. 
                     By building on your existing internal culture, seeking external perspectives could provide fresh insights that complement your approach and accelerate the pace of change, helping you stay competitive in a rapidly evolving market.''')
        if persona == 'Driver':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     You have built a strong foundation of processes that allow you to move quickly from idea to action. Your strength lies in execution—getting things done efficiently and at scale. 
                     This makes you a valuable partner in ecosystem collaborations, especially where speed and structure are crucial. 
                     To elevate your innovation capacity further, investing in building internal knowledge and capability around emerging practices and fostering leadership vision will ensure your actions are guided by strategic foresight, not just efficiency.''')
        elif persona == 'Operator':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your company has clearly established operational capabilities and leadership support that enable consistent and scalable innovation. 
                     You're good at turning ideas into real results, and your internal alignment ensures that priorities are well-executed. 
                     With this strong foundation, focusing more on developing and applying new knowledge—especially in emerging technologies and market trends—can help your organization anticipate shifts before they happen and lead the innovation curve rather than just follow it.''')
        elif persona == 'Enabler':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     You are in a strong position to translate innovative ideas into action, thanks to your balance of collaborative leadership and agile operations. 
                     Your teams work well together and are empowered by a culture that values execution and adaptability. 
                     This allows you to enable others—both inside and outside your organization—to succeed in innovation. 
                     To deepen your strategic role, focusing on knowledge development and external trend awareness can enhance your influence and help drive more forward-thinking innovation agendas.''')
        elif persona == 'Holistic Innovator':
            st.write(f'You are a **{persona}**.')
            st.write('''
                     Your organization demonstrates a rare and powerful balance across knowledge, mindset, and processes. 
                     You combine deep expertise, visionary leadership, and operational agility to lead innovation comprehensively. 
                     This balance allows you to co-create impactful solutions, scale them efficiently, and inspire your broader ecosystem. 
                     You are well-positioned to act as a role model for innovation excellence. 
                     To maintain this edge, continue refining your innovation strategy and exploring new collaboration models that push boundaries while reinforcing your strengths..''')

if 'page' not in st.session_state:
    st.session_state['page'] = 'survey'

if st.session_state['page'] == 'survey':
    survey()
elif st.session_state['page'] == 'results':
    results()