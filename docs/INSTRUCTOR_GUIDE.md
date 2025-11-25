# Workshop 3: Instructor & Facilitator Guide

**Winter University 2025 - Bayt Mal Al-Quds Asharif Agency**

**Workshop:** Approaches to Economic and Social Crises and the Protection of Cultural Heritage Using AI

---

## Table of Contents

1. [Workshop Overview](#1-workshop-overview)
2. [Pre-Workshop Preparation](#2-pre-workshop-preparation)
3. [Workshop Facilitation](#3-workshop-facilitation)
4. [Student Support](#4-student-support)
5. [Assessment Criteria](#5-assessment-criteria)
6. [Technical Support](#6-technical-support)
7. [Post-Workshop](#7-post-workshop)
8. [Appendices](#8-appendices)

---

## 1. Workshop Overview

### 1.1 Core Objectives

This workshop aims to help students:

1. **Deepen understanding** of how economic/social crises affect communities in Jerusalem and Morocco
2. **Explore digital solutions** using AI and digital platforms for crisis analysis and heritage protection
3. **Foster collaboration** between Moroccan and Palestinian students across disciplines
4. **Develop critical thinking** about technology's role in justice, dignity, and memory preservation

### 1.2 Expected Outcomes

By the end of the workshop, each student team will have:

- Identified one specific problem related to economic/social crises or heritage threats
- Formulated a clear guiding question
- Proposed a digital platform/tool concept
- Prepared and delivered a 3-5 minute presentation

### 1.3 Workshop Timeline

**Total Duration:** 2.5 - 3 hours

| Session | Duration | Activity |
|---------|----------|----------|
| Session 1 | 30 min | Introduction and team formation |
| Session 2 | 60-90 min | Problem exploration and concept development |
| Session 3 | 45-60 min | Presentation preparation and delivery |

**Flexibility Note:** Adjust timing based on number of teams and group dynamics. Plan for 3 hours to allow breathing room.

---

## 2. Pre-Workshop Preparation

### 2.1 Setting Up the Repository (1-2 hours before)

**Critical Setup Tasks:**

1. **Clone/Download the Workshop Repository**
   ```bash
   # Ensure you have the latest version
   git clone [repository-url]
   cd winter
   ```

2. **Verify File Structure**
   - Confirm all files are present and accessible
   - Check that `student-template/` folder is ready
   - Ensure `reference-dashboard/` is functional (if demoing)

3. **Test the Reference Dashboard** (Optional but recommended)
   ```bash
   cd reference-dashboard
   pip install -r requirements.txt
   streamlit run app.py
   ```
   - Verify it launches without errors
   - Familiarize yourself with key features
   - Prepare 2-3 talking points about it

4. **Prepare Distribution Method**
   - **Option A (Recommended):** Share GitHub repository link
   - **Option B:** Prepare USB drives with repository contents
   - **Option C:** Set up shared cloud folder (Google Drive, Dropbox)
   - See `/Users/musicinst/Desktop/winter/docs/DISTRIBUTION_GUIDE.md` for details

### 2.2 Preparing Materials

**Required Materials:**

- [ ] Projector/screen for presentations
- [ ] Whiteboard or flipchart for brainstorming
- [ ] Markers, sticky notes (for analog teams)
- [ ] Printed copies of key documents (optional):
  - Workshop Brief (Arabic/English/French)
  - Project Concept Template (1 per team)
- [ ] Timer or clock visible to all

**Optional Materials:**

- [ ] Example project sketches or mockups
- [ ] Printed crisis context summaries
- [ ] Index cards for team formation
- [ ] Prizes or certificates for presentations

### 2.3 Technical Setup (If Doing Live Coding/Demo)

**If You Plan to Demonstrate the Reference Dashboard:**

1. **Test Your Setup** (30 min before workshop)
   - Laptop connected to projector
   - Internet connection stable
   - Dashboard runs smoothly
   - Browser zoom appropriate for room size

2. **Prepare Backup Plan**
   - Screenshots of key dashboard features
   - PDF version of dashboard overview
   - Offline demo if internet fails

**If Students Will Code During Workshop:**

- Test that students can access repository
- Verify lab computers have Python/required software
- Have installation instructions ready
- Prepare troubleshooting cheat sheet

### 2.4 Room Setup

**Optimal Configuration:**

- **Team tables:** Clusters of 4-6 seats for collaborative work
- **Presentation area:** Clear space at front with screen/projector
- **Materials station:** Table with handouts, markers, sticky notes
- **Instructor zone:** Access to all teams for circulation

**Accessibility Considerations:**

- Ensure room is accessible to all students
- Check audio/visual accommodations if needed
- Have multilingual support available (Arabic/French/English)

### 2.5 Instructor Preparation Checklist

Personal preparation before the workshop:

- [ ] Read all workshop materials thoroughly
- [ ] Review crisis context documents (Palestine/Morocco)
- [ ] Familiarize yourself with student template structure
- [ ] Prepare opening remarks (5-7 minutes)
- [ ] Draft 3-5 example guiding questions
- [ ] Think through common challenges students might face
- [ ] Review presentation guide to help coach teams
- [ ] Prepare closing remarks and next steps

---

## 3. Workshop Facilitation

### 3.1 Session 1: Introduction and Team Formation (30 min)

#### 3.1.1 Opening Remarks (7-10 min)

**Key Messages to Convey:**

1. **Welcome and Context**
   - "Welcome to Workshop 3 on Economic Crises and Cultural Heritage Protection"
   - "You're here to think creatively about real problems affecting Jerusalem and Morocco"
   - "This is about ideas and impact, not perfect technical execution"

2. **Workshop Objectives**
   - Explain the three main goals (see 1.1)
   - Emphasize collaboration across borders and disciplines
   - Highlight that presentations are learning opportunities, not competitions

3. **What Success Looks Like**
   - Clear problem identification
   - Thoughtful, context-aware solution concept
   - Strong presentation that communicates impact
   - Team collaboration and learning

4. **Timeline Overview**
   - Walk through the 3 sessions
   - Show where materials are located
   - Explain presentation format (3-5 min per team)

**Example Opening Script:**

> "Good morning/afternoon everyone. Welcome to Workshop 3 of the Winter University. Over the next few hours, you'll work in mixed Moroccan-Palestinian teams to tackle real challenges facing communities in crisis.
>
> Your task is not to build a perfect technical solution - it's to think deeply about a specific problem and propose a thoughtful digital platform concept that could make a difference. Some of you come from technical backgrounds, others from humanities or social sciences. That diversity is your strength.
>
> By the end of today, each team will present a 3-5 minute concept. We're looking for clarity, creativity, and impact. Let's get started."

#### 3.1.2 Quick Reference Dashboard Demo (5-7 min) - OPTIONAL

**If You Choose to Demo:**

1. **Launch the dashboard** and show homepage
2. **Navigate to 2-3 key pages**:
   - Context & Background (show research integration)
   - Macro-Economic Indicators (show interactivity)
   - One scenario modeling page (show sliders/controls)

3. **Key Points to Emphasize**:
   - "This is ONE example of what's possible"
   - "Your project can be much simpler"
   - "Notice how it addresses a specific research question"
   - "See how data visualization helps tell a story"

4. **Avoid:**
   - Getting lost in technical details
   - Implying students must replicate this
   - Spending more than 7 minutes on demo

**If You Skip the Demo:**

Simply point students to the reference dashboard folder and let them explore it optionally during their work time.

#### 3.1.3 Team Formation (15-18 min)

**Goal:** Form 4-6 mixed teams (Moroccan-Palestinian, interdisciplinary)

**Method 1: Structured Assignment** (Recommended if time-limited)

1. **Pre-assign teams** based on:
   - Mix of nationalities (Moroccan + Palestinian)
   - Mix of disciplines (tech + humanities + social science)
   - Balanced skill levels

2. **Announce teams** and have students move to their tables

3. **Icebreaker prompt** (5 min):
   - "Introduce yourself: Name, field of study, one skill you bring to the team"
   - "Share one thing that surprised you about crises in Jerusalem or Morocco"

**Method 2: Self-Organization** (Better for engagement, takes longer)

1. **Call out disciplines**:
   - "Raise your hand if you study: Technology/AI, Social Sciences, Humanities, Heritage/Architecture, Media, Other"

2. **Guided mixing**:
   - "We need teams of 4-5 with at least one person from Morocco and one from Palestine"
   - "Try to mix disciplines - tech people, find some humanities folks!"

3. **Let students mingle** for 10 minutes to form teams

4. **Verify teams** are mixed and balanced

**Team Formation Tips:**

- Aim for 4-5 students per team (not more than 6)
- Ensure no team is all from one country
- Encourage mix of technical and non-technical students
- Have a backup plan for solo students or odd numbers
- Appoint a "team captain" or spokesperson early

---

### 3.2 Session 2: Problem Exploration and Concept Development (60-90 min)

#### 3.2.1 Launching the Work Session (5 min)

**Instructions to Teams:**

1. **Introduce the Student Template**
   - "Navigate to `student-template/` folder"
   - "Start by reading the README.md"
   - "Use `project-concept.md` as your working document"

2. **Outline the Process**
   - "Step 1: Choose a specific problem (15 min)"
   - "Step 2: Define your guiding question (10 min)"
   - "Step 3: Brainstorm platform concept (20-30 min)"
   - "Step 4: Fill out project concept template (15-20 min)"

3. **Resources Available**
   - Point to `student-template/resources/` folder
   - Mention you'll circulate to answer questions
   - Clarify when you'll give a "30-minute warning"

4. **Encourage Exploration**
   - "There's no single right answer"
   - "Start broad, then narrow down"
   - "Think about real people using your tool"

#### 3.2.2 Circulating Among Teams (50-70 min)

**Your Role:**

- Visit each team 2-3 times during the session
- Spend 5-7 minutes per visit
- Ask guiding questions (see 4.2)
- Nudge without dictating solutions
- Track which teams are struggling vs. thriving

**First Visit (10-15 min into session):**

Focus on problem selection:

- "What problem are you exploring?"
- "Who is affected by this problem?"
- "Can you narrow it down to be more specific?"

**Second Visit (30-40 min into session):**

Focus on solution concept:

- "What type of platform are you thinking about?"
- "Who would use it, and how?"
- "What makes your idea different or valuable?"

**Third Visit (50-60 min into session):**

Focus on clarity and impact:

- "Can you explain your idea in one sentence?"
- "What's the main impact you expect?"
- "Are you ready to start working on your presentation?"

#### 3.2.3 Time Checkpoints

**30 Minutes In:**

- "Teams, you should be finalizing your problem statement"
- "If you're still brainstorming, start narrowing down now"

**45 Minutes In:**

- "You should have a clear guiding question and platform concept"
- "If not, simplify - pick the clearest idea and run with it"

**60 Minutes In:**

- "30 minutes left in this session"
- "Start filling out your project concept template"
- "Think about how you'll present this"

**75-80 Minutes In:**

- "Wrap up concept development"
- "Get ready to move to presentation prep"

#### 3.2.4 Common Challenges and Interventions

See Section 4.3 for detailed strategies.

**Quick interventions:**

| Challenge | Quick Fix |
|-----------|-----------|
| Team stuck on problem choice | "Pick the one that affects the most people" |
| Idea too broad/ambitious | "Focus on just ONE user group and ONE key feature" |
| Team not collaborating | "Let's do a quick round: everyone shares one idea in 30 seconds" |
| Technical barriers | "Don't worry about HOW to build it - focus on WHAT it should do" |
| Low energy/engagement | "Let me share an example to spark ideas..." |

---

### 3.3 Session 3: Presentation Preparation and Delivery (45-60 min)

#### 3.3.1 Transition to Presentations (2 min)

**Announce:**

- "Great work on concept development!"
- "Now you have 15-20 minutes to prepare your 3-5 minute presentation"
- "Remember the structure from the presentation guide"
- "Decide who will present which parts"

#### 3.3.2 Presentation Preparation Time (15-20 min)

**Teams should:**

- Review their completed project-concept.md
- Decide on speaking roles (all members should participate)
- Practice timing (3-5 minutes)
- Create simple visual aids if desired (sketch, slide, poster)
- Rehearse at least once

**Your Role:**

- Circulate to answer last-minute questions
- Help teams who are running long to cut content
- Encourage quiet/shy students to take a role
- Verify presentation order

**5-Minute Warning:**

- "5 minutes left - practice your full presentation once"
- "Make sure everyone knows their part"

#### 3.3.3 Presentations (25-40 min)

**Setup:**

- Arrange seating so all can see presenting team
- Have timer visible
- Set up any A/V equipment needed

**Presentation Protocol:**

1. **Introduce presenting team** (you or team captain)
2. **Team presents** (3-5 minutes)
3. **Brief Q&A** (1-2 questions, 2-3 minutes)
4. **Thank team and transition** (30 seconds)

**Timing:**

- 5-6 teams x 6-8 minutes each = 30-48 minutes
- Build in buffer time for transitions

**Your Role During Presentations:**

- Time each presentation discreetly
- Take notes on strengths and areas for feedback
- Model engaged listening for other students
- Prepare 1-2 questions per team (if time allows)

**If a Team Runs Over Time:**

- Give a subtle signal at 5 minutes (hold up hand)
- Don't interrupt unless they're severely over (7+ min)
- Address timing in general feedback, not singling them out

#### 3.3.4 Q&A Guidelines

**Good Questions to Ask:**

- "Can you say more about who would use this tool?"
- "What's one challenge you might face implementing this?"
- "How would you measure if your platform is successful?"
- "What inspired this particular approach?"

**Questions to Avoid:**

- Anything that sounds like criticism ("Why didn't you consider X?")
- Overly technical implementation details
- Questions that put students on the spot negatively

**Encouraging Peer Questions:**

- "Does anyone have a question for this team?"
- "What did you find most interesting about this concept?"

---

### 3.4 Closing and Wrap-Up (5-10 min)

#### 3.4.1 General Feedback

**Highlight Patterns You Noticed:**

- "I saw great creativity in how you approached [theme]"
- "Many teams focused on [common element] - that shows you identified a key need"
- "I appreciated the diversity of ideas - from [example 1] to [example 2]"

**Celebrate Strengths:**

- Acknowledge specific strong moments (without ranking teams)
- Praise collaboration and interdisciplinary thinking
- Recognize courage in presenting

**Gentle Areas for Growth:**

- "In future presentations, think about showing a simple sketch or mockup"
- "Remember to emphasize the human impact, not just features"
- "Practice timing - it's a skill that comes with repetition"

#### 3.4.2 Key Takeaways

**Reinforce:**

1. **Contextual Thinking**
   - "You showed deep understanding of crisis contexts"
   - "Your solutions were grounded in real community needs"

2. **Technology as Tool**
   - "Technology is powerful, but it serves people and purposes"
   - "The best digital tools are designed WITH communities, not FOR them"

3. **Interdisciplinary Collaboration**
   - "Mixing technical and humanistic perspectives made your ideas stronger"
   - "Keep seeking diverse perspectives in your future work"

#### 3.4.3 Next Steps

**If Projects Will Continue:**

- Explain how students can develop their concepts further
- Provide resources for learning relevant technical skills
- Offer office hours or follow-up support
- Mention potential showcases or competitions

**If This is a Standalone Workshop:**

- Encourage students to add this to their portfolios
- Suggest sharing with professors or potential collaborators
- Provide readings on crisis informatics / humanitarian tech

**Closing Remarks:**

> "Thank you all for your engagement today. You've shown that young people from different backgrounds, working together, can imagine powerful solutions to some of the most pressing challenges facing our region. Whether or not you pursue these exact projects, carry forward this collaborative spirit and this commitment to using your skills for justice and dignity. Thank you."

---

## 4. Student Support

### 4.1 Common Questions and Answers

#### General Questions

**Q: "Do we have to build a working application?"**

A: "No. You're creating a concept, not a finished product. Focus on clearly explaining what your platform would do, who would use it, and why it matters."

**Q: "Can we work on a problem from Morocco instead of Jerusalem?"**

A: "Yes, as long as you can connect it to the workshop themes of economic/social crises or heritage protection. Jerusalem should be the primary focus, but Moroccan parallels are encouraged."

**Q: "What if we don't know anything about technology?"**

A: "That's fine. Your job is to understand the problem and the users. Think about WHAT the tool should do, not HOW to build it technically."

**Q: "Can we propose something that already exists?"**

A: "You can build on existing platforms, but explain what's unique about your approach or how you'd adapt it to this specific context."

#### Technical Questions

**Q: "What programming language should we use?"**

A: "You don't need to write code for this workshop. If you want to in the future, Python (for data tools) or JavaScript (for web apps) are good starting points."

**Q: "How would we get the data for our platform?"**

A: "Good question. Think about: government databases, NGO reports, user-generated data, satellite imagery, social media, sensors, etc. Be specific about what data you need and realistic about what's available."

**Q: "What if there's no internet access in crisis zones?"**

A: "Excellent consideration. You might propose: offline-first design, SMS-based systems, periodic syncing when connection is available, or low-bandwidth solutions."

#### Concept Questions

**Q: "Our idea feels too simple. Is that okay?"**

A: "Simple is good. A well-executed simple idea is better than a complicated one that doesn't work. If it solves a real problem clearly, it's valuable."

**Q: "Can we combine multiple ideas?"**

A: "You can, but be careful not to make it too complicated. It's better to do one thing really well than many things poorly."

**Q: "What if our idea might not work in practice?"**

A: "Acknowledge the challenges. Part of good design is understanding limitations. Propose how you might address them or what you'd need to test."

### 4.2 Guiding Questions (Without Dictating Solutions)

#### For Problem Selection

**Instead of:** "You should focus on checkpoint delays."

**Try:**
- "What's the most urgent problem facing people in this crisis?"
- "If you could help one group of people, who would it be?"
- "What problem keeps you up at night when you think about this situation?"
- "Which problem, if solved, would create the biggest positive change?"

#### For Solution Development

**Instead of:** "You should build a mobile app."

**Try:**
- "How do people currently try to solve this problem?"
- "What tools or information do they lack?"
- "If you could give affected communities one digital tool, what would it do?"
- "How would someone actually use this in a crisis moment?"

#### For Clarity and Focus

**Instead of:** "That's too broad."

**Try:**
- "Can you give me a specific example of how this would work?"
- "Tell me about ONE person who would use this. What's their day like?"
- "What's the MAIN thing your platform does?"
- "If you could only have one feature, what would it be?"

#### For Impact Thinking

**Instead of:** "That won't work."

**Try:**
- "What would success look like for this platform?"
- "How would you know if this is helping people?"
- "What would change for communities if this existed?"
- "What challenges might you face, and how could you address them?"

### 4.3 Helping Teams That Are Stuck

#### Stuck on Problem Selection

**Symptoms:**
- Debating many different problems
- Can't agree on focus
- Everything feels equally important

**Intervention:**
1. "Let's take 2 minutes: everyone write down ONE problem on a sticky note"
2. "Put them on the table and group similar ones"
3. "Vote: which affects the most people or feels most urgent?"
4. "Go with that one - you can explore others later"

**Prompts to Help:**
- "Think about a specific person or place you know"
- "What did you find most striking in the crisis context readings?"
- "Is there a problem that connects to your own field of study?"

#### Stuck on Solution Concept

**Symptoms:**
- Vague descriptions ("make things better")
- Can't articulate how it works
- Ideas keep changing

**Intervention:**
1. "Close your eyes and imagine: a person is using your tool. What do they SEE on the screen?"
2. "Walk me through: they open it, then what? What happens next?"
3. "What's the one main action your tool enables?"

**Prompts to Help:**
- "Think about apps you use every day - what makes them useful?"
- "If you had to explain this to your grandmother, what would you say?"
- "What's the simplest version of this idea?"

#### Stuck on Team Dynamics

**Symptoms:**
- One person dominating
- Silent members not participating
- Disagreements or tension

**Intervention:**
1. **For dominant member:** "Great ideas, [Name]. Let's hear from everyone. [Quiet person], what do you think?"
2. **For silent members:** "I notice some folks haven't shared yet. Let's do a round where everyone says one thing."
3. **For disagreements:** "You have two good ideas. Can you combine them, or test both and see which resonates?"

**Prompts to Help:**
- "What does each person bring to this team? Name one strength per member."
- "Let's divide tasks: who wants to focus on problem research? Who wants to sketch the platform?"
- "Take 5 minutes for individual brainstorming, then come back together"

#### Stuck on Presentations

**Symptoms:**
- Can't fit everything into 3-5 minutes
- Not sure who should speak
- Nervous about public speaking

**Intervention:**
1. "Your presentation should answer: What's the problem? What's your solution? Why does it matter? That's it."
2. "Divide it up: Person A introduces problem (1 min), Person B explains solution (2 min), Person C describes impact (1 min)"
3. "Practice once out loud right now - I'll time you"

**Prompts to Help:**
- "What's the ONE thing you want people to remember about your idea?"
- "Imagine you're explaining this to a funder who can give you money - what would you say?"
- "It's okay to be nervous - just speak clearly and support each other"

---

## 5. Assessment Criteria

### 5.1 What Makes a Good Project Concept

**Excellent concepts demonstrate:**

1. **Specificity**
   - Clear problem statement (not "poverty" but "small merchants can't access microloans during closures")
   - Defined user group (not "everyone" but "shop owners in East Jerusalem Old City aged 40-60")
   - Concrete platform features (not "shares information" but "sends SMS alerts about checkpoint openings")

2. **Context Awareness**
   - Shows understanding of crisis dynamics
   - Considers local constraints (internet access, literacy, trust in tech)
   - Respects cultural and political sensitivities

3. **Feasibility**
   - Realistic about what's achievable
   - Considers data sources and availability
   - Acknowledges limitations or challenges

4. **Impact Orientation**
   - Clear about who benefits and how
   - Explains expected outcomes
   - Connects to broader themes (resilience, dignity, memory)

5. **Creativity**
   - Original angle or approach
   - Thoughtful combination of technologies
   - Human-centered design thinking

### 5.2 Presentation Evaluation Points

**Strong presentations include:**

| Criterion | What to Look For | Weight |
|-----------|------------------|--------|
| **Clarity** | Easy to understand, well-structured, jargon-free | 25% |
| **Problem Articulation** | Specific problem, who's affected, why it matters | 20% |
| **Solution Quality** | Clear concept, defined features, realistic approach | 25% |
| **Impact Thinking** | Explains benefits, considers success metrics | 15% |
| **Team Collaboration** | All members participate, coherent delivery | 10% |
| **Engagement** | Captures attention, good pacing, handles Q&A | 5% |

### 5.3 Evaluation Rubric (If Grading Required)

**4-Point Scale:**

**4 - Excellent**
- Addresses all criteria at high level
- Demonstrates deep understanding and creativity
- Clear, compelling presentation
- Strong team collaboration evident

**3 - Good**
- Addresses most criteria well
- Shows solid understanding of context
- Clear presentation with minor gaps
- Good team participation

**2 - Satisfactory**
- Addresses basic criteria
- Some understanding of context, but surface-level
- Presentation lacks clarity or structure
- Uneven team participation

**1 - Needs Improvement**
- Missing key criteria
- Limited understanding of context
- Unclear presentation
- Minimal team collaboration

### 5.4 Providing Feedback

**Feedback Formula:**

1. **Specific Praise** - "I really appreciated how you..."
2. **Clarifying Question** - "Can you tell me more about..."
3. **Constructive Suggestion** - "One way to strengthen this could be..."
4. **Encouragement** - "This has real potential, especially..."

**Example:**

> "Team 3, I really appreciated how you focused on a specific neighborhood and user group - that made your concept very concrete. Can you tell me more about how you'd handle data privacy for families sharing location information? One way to strengthen this could be exploring existing privacy frameworks in humanitarian tech. This has real potential, especially if you partner with local NGOs who already have community trust."

**What to Emphasize in Feedback:**

- Process (collaborative thinking) over product (perfect solution)
- Critical thinking about context
- Creativity and originality
- Growth and learning

---

## 6. Technical Support

### 6.1 Helping Students with the Reference Dashboard

#### 6.1.1 When to Recommend the Dashboard

**Good scenarios:**
- Team wants to see what's possible with data visualization
- Team is considering a dashboard-style platform
- Team needs inspiration for structuring data
- Team wants to understand Streamlit or Python basics

**Less helpful scenarios:**
- Team is overwhelmed and needs simplification (don't add more complexity)
- Team is focused on mobile apps or non-dashboard tools
- Very limited time remaining

#### 6.1.2 Guided Dashboard Tour

**5-Minute Tour Structure:**

1. **Homepage** (1 min)
   - "This is a Streamlit app - a Python framework for data apps"
   - "Notice the sidebar navigation - simple and clear"

2. **Context Page** (2 min)
   - "See how research is integrated into the app"
   - "Data + narrative = powerful storytelling"

3. **Interactive Page** (2 min)
   - "Try adjusting these sliders - see how the chart updates?"
   - "Interactivity helps users explore scenarios"

**Key Points:**
- "This took weeks to build - your concept can be MUCH simpler"
- "Notice how each page answers ONE clear question"
- "See how they explain WHY the data matters, not just show numbers"

#### 6.1.3 Common Dashboard Questions

**Q: "Can we use this code for our project?"**

A: "You can explore it for learning, but you're not required to code anything for this workshop. If you want to build something later, this is a good reference."

**Q: "How do we make our own dashboard?"**

A: "After the workshop, you could: 1) Learn Python basics, 2) Learn Streamlit through their tutorials, 3) Start with a simple one-page app, 4) Add features gradually. But today, focus on your concept, not the coding."

**Q: "Where does the data come from?"**

A: "Check the `data/` folder - it's CSV files. The dashboard loads and visualizes them. For your concept, think about what data YOU would need and where you'd get it."

### 6.2 Troubleshooting Common Issues

#### Repository Access Problems

**Issue:** "I can't access the repository."

**Solutions:**
- Verify GitHub link is correct and public
- Try accessing from different browser
- Download as ZIP file instead of cloning
- Share via USB drive as backup

**Issue:** "Files won't open."

**Solutions:**
- Ensure they're using a text editor (VSCode, Sublime) or markdown viewer
- GitHub preview should work for .md files
- Open in browser if other methods fail

#### Dashboard Won't Run

**Issue:** "I get an error when running the dashboard."

**Common Causes & Fixes:**

| Error | Cause | Fix |
|-------|-------|-----|
| "streamlit not found" | Not installed | `pip install streamlit` |
| "pandas not found" | Not installed | `pip install -r requirements.txt` |
| "No such file or directory" | Wrong folder | `cd reference-dashboard` first |
| "Port already in use" | Streamlit already running | Close other instance or use `--server.port 8502` |

**Quick Diagnostic:**
```bash
# Check Python is installed
python --version

# Check if in correct directory
ls  # Should see app.py

# Check dependencies
pip list | grep streamlit
```

#### Markdown Files Display Issues

**Issue:** "The .md files look weird."

**Solutions:**
- View on GitHub (renders nicely)
- Use VSCode with Markdown Preview
- Open in specialized markdown editor (Typora, MacDown)
- Convert to PDF if needed

### 6.3 Technical Questions Quick Reference

**Platform Types:**

| Platform Type | Best For | Examples to Share |
|---------------|----------|-------------------|
| Mobile App | On-the-go access, location services, notifications | Waze, WhatsApp, Ushahidi |
| Website/Web App | Broad access, no installation, works on any device | Google Maps, Facebook, Crisis Mappers |
| Dashboard | Data visualization, analysis, decision support | Reference dashboard, Tableau, Power BI |
| SMS/Text Service | Low-tech access, works without internet | Textit, RapidPro, UNICEF U-Report |
| Chatbot | Interactive Q&A, guided assistance | Crisis support bots, info hotlines |

**Data Sources for Crises:**

- Government statistics (PCBS, World Bank)
- NGO reports (UN OCHA, humanitarian organizations)
- User-generated reports (crowdsourcing)
- Satellite imagery (Google Earth Engine, Sentinel)
- Social media (Twitter, Facebook - with ethics considerations)
- Sensor data (IoT, environmental monitors)
- Surveys and field research

**Technologies to Mention (if asked):**

- **For web apps:** HTML/CSS/JavaScript, React, Vue
- **For mobile apps:** Flutter, React Native, Swift (iOS), Kotlin (Android)
- **For dashboards:** Streamlit, Dash, Tableau, Power BI
- **For AI/ML:** Python, TensorFlow, scikit-learn
- **For data:** Pandas, NumPy, SQL databases
- **For maps:** Leaflet, Mapbox, Google Maps API

---

## 7. Post-Workshop

### 7.1 Follow-Up Suggestions

#### Immediate Follow-Up (Within 1 Week)

**For All Students:**

1. **Share Resources**
   - Email with repository link
   - Links to relevant readings on crisis informatics
   - List of online courses (Coursera, edX) on relevant topics
   - Contact information for questions

2. **Collect Feedback**
   - Send brief survey (5-7 questions)
   - Ask what worked well and what could improve
   - Gather suggestions for future workshops

3. **Provide Summary**
   - Recap of all team concepts (1-2 sentences each)
   - Key takeaways from the workshop
   - Acknowledgment of their work

**For Interested Students:**

4. **Office Hours**
   - Offer 1-2 time slots for follow-up questions
   - Can be in-person or virtual

5. **Additional Resources**
   - Curated list of readings on their specific topics
   - Connections to relevant professors or practitioners
   - Information about related opportunities (internships, competitions)

#### Medium-Term Follow-Up (1-4 Weeks)

**Optional Activities:**

1. **Showcase Event**
   - Host presentation session for broader audience
   - Invite faculty, NGOs, potential partners
   - Record presentations for portfolio use

2. **Project Development Workshop**
   - Optional follow-up session for teams who want to continue
   - Focus on next steps: prototyping, user research, technical planning

3. **Guest Speaker**
   - Invite practitioner in humanitarian tech or crisis informatics
   - Have them review student concepts and provide feedback

4. **Competition/Publication**
   - Encourage strong teams to submit to conferences (CHI, ISCRAM)
   - Apply to innovation competitions
   - Write up as case studies for publication

#### Long-Term Follow-Up (1-6 Months)

**Sustaining Interest:**

1. **Alumni Network**
   - Create listserv or WhatsApp group for workshop alumni
   - Share opportunities, news, resources

2. **Mentorship**
   - Connect students with mentors in their areas of interest
   - Facilitate partnerships with NGOs or research groups

3. **Showcase Success**
   - Highlight teams who've developed their projects further
   - Share on university website, social media
   - Use as recruiting tool for future workshops

### 7.2 How Students Can Develop Projects Further

**Provide a "Next Steps" Roadmap:**

#### Phase 1: Validate the Concept (Weeks 1-4)

**Activities:**
- **User research:** Interview 5-10 potential users
- **Competitive analysis:** What similar tools exist? What's missing?
- **Refine scope:** Based on feedback, narrow or adjust focus
- **Sketch mockups:** Create simple wireframes or sketches

**Resources to Share:**
- User interview guides (Design Kit, IDEO)
- Mockup tools (Figma, Balsamiq, even paper & pen)
- Case studies of humanitarian tech projects

#### Phase 2: Prototype (Weeks 5-12)

**Activities:**
- **Build minimum viable product (MVP):** Simplest version that works
- **Test with users:** Show prototype, gather feedback
- **Iterate:** Make improvements based on testing
- **Document lessons learned**

**Resources to Share:**
- No-code tools (Bubble, Glide, Airtable)
- Coding tutorials (Python, JavaScript, mobile dev)
- Prototyping best practices
- Testing frameworks

#### Phase 3: Pilot and Scale (Months 4-6+)

**Activities:**
- **Pilot with real users:** Deploy to small user group
- **Measure impact:** Track usage, gather testimonials
- **Seek partnerships:** NGOs, government agencies, funders
- **Plan for sustainability:** How to maintain and fund long-term?

**Resources to Share:**
- Grant databases (humanitarian tech funding)
- Partnership frameworks (MOUs, collaboration agreements)
- Impact measurement guides
- Sustainability models (freemium, donation, grant-based)

### 7.3 Recommended Resources

#### Crisis Informatics & Humanitarian Tech

**Books:**
- *Crisis Informatics* by Amanda L. Hughes & Leysia Palen
- *Design for the Real World* by Victor Papanek
- *Small Things Considered* by Henry Petroski

**Websites & Organizations:**
- Crisis Mappers Network
- ISCRAM (Information Systems for Crisis Response and Management)
- OCHA Centre for Humanitarian Data
- UNHCR Innovation Service
- Missing Maps Project

**Online Courses:**
- Coursera: "Humanitarian Aid and Development"
- edX: "Data Science for Social Good"
- Humanitarian Academy: "Introduction to Humanitarian Action"

#### Technical Skills

**For Non-Coders:**
- Codecademy: "Learn Python" (free basics)
- FreeCodeCamp: Web development
- Google's Digital Garage: Digital skills

**For Designers:**
- Interaction Design Foundation courses
- UX Design courses (Coursera, LinkedIn Learning)
- Figma tutorials (free tool + learning resources)

**For Data Science:**
- DataCamp: Python for Data Science
- Kaggle: Learn and practice with real datasets
- Towards Data Science (blog)

#### Context-Specific Resources

**Palestine/Jerusalem:**
- Palestinian Central Bureau of Statistics (PCBS)
- Applied Research Institute Jerusalem (ARIJ)
- B'Tselem: Data on occupation impacts

**Morocco:**
- Haut-Commissariat au Plan (HCP) - statistics
- World Bank Morocco data
- Climate & migration studies

### 7.4 Facilitator Self-Reflection

**After the workshop, take 15-30 minutes to reflect:**

**What Went Well:**
- Which teams produced strongest concepts? Why?
- Which facilitation strategies worked best?
- What moments had highest engagement?

**What to Improve:**
- Which teams struggled? What support was missing?
- What timing adjustments would help?
- What additional resources would be useful?

**Lessons for Next Time:**
- What questions came up repeatedly? (Add to FAQ)
- What materials need updating?
- What new examples or case studies to include?

**Document:**
- Save notes for future workshops
- Update this guide with lessons learned
- Share insights with fellow instructors

---

## 8. Appendices

### Appendix A: Sample Workshop Schedule

**Full 3-Hour Workshop Timeline:**

| Time | Duration | Activity | Materials Needed |
|------|----------|----------|------------------|
| 0:00 - 0:10 | 10 min | Arrival, setup, welcome | Name tags, seating chart |
| 0:10 - 0:20 | 10 min | Opening remarks | Slides (optional) |
| 0:20 - 0:27 | 7 min | Reference dashboard demo (optional) | Laptop, projector |
| 0:27 - 0:45 | 18 min | Team formation & icebreaker | Team assignment cards |
| 0:45 - 0:50 | 5 min | Introduce work session | Whiteboard for instructions |
| 0:50 - 2:00 | 70 min | Concept development work time | Student templates, resources |
| - 1:05 | - | Check-in: Problem selection | - |
| - 1:20 | - | Check-in: Solution concept | - |
| - 1:45 | - | 15-min warning | - |
| 2:00 - 2:20 | 20 min | Presentation preparation | Timer, A/V setup |
| 2:20 - 2:22 | 2 min | Transition to presentations | Seating rearrangement |
| 2:22 - 2:52 | 30 min | Team presentations (5 teams × 6 min) | Timer, Q&A prompts |
| 2:52 - 3:00 | 8 min | Feedback, closing remarks, next steps | Handout with resources |

**Notes:**
- Add 15-30 min buffer for larger groups or more teams
- Can compress demo or extend work time as needed
- Allow breaks if workshop exceeds 2.5 hours

### Appendix B: Example Problem Statements

**Strong Problem Statements:**

1. **Checkpoint Access (Palestine)**
   - "Workers from East Jerusalem cannot predict when checkpoints will open, causing job loss and economic hardship for families dependent on wage labor in Israel."

2. **Heritage Documentation (Jerusalem)**
   - "Traditional craftspeople in the Old City lack a digital platform to document and preserve their techniques, risking loss of intangible heritage as master craftspeople age."

3. **Climate Migration (Morocco)**
   - "Rural youth migrating to cities lack information about housing, jobs, and services, leading to vulnerability and exploitation."

4. **Institutional Resilience (Jerusalem)**
   - "Cultural institutions facing economic pressure have no centralized system to share resources, coordinate programming, or pool funding applications."

5. **Historical Narrative Preservation**
   - "Families displaced from neighborhoods lack a collective archive to preserve stories, photos, and memories of their communities before displacement."

**Weak Problem Statements (and How to Improve):**

| Weak | Why It's Weak | Improved Version |
|------|---------------|------------------|
| "Poverty in Palestine" | Too broad, no specific user | "Shop owners in East Jerusalem Old City struggle to access microloans during prolonged closures" |
| "People need help" | Vague, no clear problem | "Elderly residents cannot access medical care when transport is disrupted by checkpoints" |
| "Save cultural heritage" | Noble but unfocused | "Vernacular architecture in Silwan is being demolished faster than it can be documented" |
| "Crisis communication" | Generic, applicable anywhere | "During sudden closures, parents cannot locate children who attend school across checkpoints" |

### Appendix C: Platform Concept Examples

**Example 1: Checkpoint Navigator (Mobile App)**

- **Problem:** Unpredictable checkpoint delays
- **Users:** Daily commuters (workers, students)
- **Key Features:**
  - Real-time checkpoint status (open/closed/delays)
  - Crowdsourced updates from users
  - Alternative route suggestions
  - Push notifications for sudden closures
- **Impact:** Reduced wait times, better planning, less economic loss

**Example 2: Heritage Archive (Web Platform)**

- **Problem:** Loss of oral histories and cultural practices
- **Users:** Community elders, researchers, youth
- **Key Features:**
  - Video/audio upload interface
  - Tagging by neighborhood, time period, theme
  - Multi-language support (Arabic, English, Hebrew)
  - Private/public sharing controls
- **Impact:** Preserved memory, educational resource, counter-narratives

**Example 3: Resource Coordination Network (Dashboard)**

- **Problem:** Fragmented institutional responses to crisis
- **Users:** NGOs, cultural institutions, aid organizations
- **Key Features:**
  - Shared calendar of events and needs
  - Funding opportunity aggregator
  - Collaboration matchmaking
  - Impact metrics tracking
- **Impact:** Reduced duplication, stronger partnerships, better resource allocation

**Example 4: Climate Adaptation Toolkit (SMS + Web)**

- **Problem:** Rural farmers lack climate resilience information
- **Users:** Small-scale farmers in Morocco
- **Key Features:**
  - SMS alerts for weather and drought forecasts
  - Adaptation technique library (low-water crops, soil conservation)
  - Market prices for alternative crops
  - Peer learning forum
- **Impact:** Reduced crop loss, income diversification, community knowledge sharing

### Appendix D: Facilitation Cheat Sheet

**Quick Reference for In-the-Moment Decisions:**

#### Time Management Signals

| Time Remaining | What to Do |
|----------------|------------|
| 60 min | "You should be selecting your problem now" |
| 45 min | "Start narrowing to a specific guiding question" |
| 30 min | "Focus on platform concept - what it is, who uses it" |
| 15 min | "Wrap up concept work, prepare for presentations" |
| 5 min | "Final touches, practice your timing" |

#### Energy Level Interventions

| Energy Level | Intervention |
|--------------|--------------|
| Low/Sluggish | Stand-up stretch, share an inspiring example, pose provocative question |
| Chaotic/Scattered | Refocus attention, give clear next step, set mini-deadline |
| Uneven (some engaged, some not) | Rotate roles, pair quiet with talkative, give individual tasks |

#### Question Response Framework

| Question Type | Response Strategy |
|---------------|-------------------|
| Technical ("How do we code this?") | "You don't need to code today - focus on WHAT not HOW" |
| Perfectionist ("Is this good enough?") | "If it solves the problem clearly, yes. Simple is good" |
| Lost ("We don't know what to do") | Ask 3 guiding questions, have them choose one to start |
| Overly Ambitious ("We want to do everything") | "Pick the ONE most important feature. You can always add later" |

#### Red Flags to Watch For

| Red Flag | Action |
|----------|--------|
| Team silent for 5+ minutes | Visit, ask "What's the blocker?" |
| One person typing, others disengaged | "Let's have everyone contribute - how about each person shares one idea?" |
| Heated disagreement | "You both have good points. Can we try [compromise]?" |
| Off-topic conversation | Gentle redirect: "Great discussion, but let's focus on the problem for now" |
| Team finished early (30+ min left) | "Dig deeper: Who exactly would use this? What challenges might arise?" |

### Appendix E: Multilingual Support Tips

**Workshop Language Considerations:**

The workshop materials are available in:
- Arabic (العربية)
- English
- French (Français)

**Facilitation Strategies:**

1. **Mixed-Language Teams**
   - Encourage teams to work in language they're most comfortable with
   - Allow presentations in any of the three languages
   - Have multilingual facilitators if possible

2. **Key Terms Translation**
   - Provide glossary of key terms in all three languages
   - Use visual aids to transcend language barriers
   - Encourage teams to create bilingual/trilingual presentations

3. **Translation Support**
   - Pair students who speak different languages
   - Use online translation tools as backup (Google Translate)
   - Summarize key points in multiple languages during wrap-up

**Common Terms Glossary:**

| English | العربية (Arabic) | Français (French) |
|---------|------------------|-------------------|
| Crisis | أزمة | Crise |
| Heritage | تراث | Patrimoine |
| Platform | منصة | Plateforme |
| Dashboard | لوحة معلومات | Tableau de bord |
| User | مستخدم | Utilisateur |
| Impact | تأثير | Impact |
| Resilience | صمود | Résilience |
| Digital tool | أداة رقمية | Outil numérique |
| Checkpoint | حاجز | Point de contrôle |

---

## Final Notes for Facilitators

**Remember:**

1. **Your role is to guide, not dictate**
   - Students learn best through discovery
   - Resist the urge to solve problems for them
   - Ask questions that lead them to insights

2. **Emphasize process over product**
   - The learning is in the thinking and collaboration
   - A "failed" concept that taught them something is more valuable than a polished one they didn't engage with

3. **Create a safe learning environment**
   - Normalize uncertainty and iteration
   - Celebrate effort and creativity
   - Make it okay to not have all the answers

4. **Be flexible**
   - This guide is a framework, not a script
   - Adapt to your specific group's needs and energy
   - Trust your instincts about pacing and interventions

5. **Model the values**
   - Collaborative thinking
   - Respect for diverse perspectives
   - Critical engagement with technology
   - Commitment to justice and dignity

**You've got this. Your facilitation makes this workshop meaningful. Thank you for your commitment to these students and these important questions.**

---

**Document Information:**

- **Created:** November 2024
- **Last Updated:** November 2024
- **Version:** 1.0
- **Contact:** [Workshop coordinator contact information]
- **Related Documents:**
  - `/Users/musicinst/Desktop/winter/WORKSHOP_BRIEF.md`
  - `/Users/musicinst/Desktop/winter/student-template/README.md`
  - `/Users/musicinst/Desktop/winter/docs/DISTRIBUTION_GUIDE.md`
