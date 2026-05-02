import streamlit as st
import facade
from facade.lucide import icon_html

st.set_page_config(
    page_title="streamlit-facade demo",
    page_icon="assets/mark.png",
    layout="wide",    
)

facade.theme.apply(
    preset="carbon-sage",
    base="light",
    font_sans="DM Sans",
    font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700",
    radius="xl",   
)

# Session Stage
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navbar
nav_logo, nav_space, nav_buttons = st.columns([3, 6, 2], vertical_alignment="center")

with nav_logo:
    st.logo('assets/mark.png', size="large")

if st.session_state.page == "Home":
    col1,col2,col3 = st.columns([3,4,3])
    with col2:
        with st.container(horizontal_alignment="center", width="stretch"):
            st.markdown(":primary-badge[shadcn inspired · pure Python · built with Facade]",text_alignment="center")
            st.markdown("# Facade is Streamlit, :primary[but different.]",text_alignment="center")
            st.space(size="small")
            st.markdown("### A themeable UI component library for Streamlit. One theme call, every component picks up your colors, font, and radius automatically.",text_alignment="center")
            st.image('assets/pypi.png', width=500)
            with st.container(horizontal=True, horizontal_alignment="center", width="content", gap='xxsmall'):
                if facade.Button("Docs", variant="default", key="nav_docs", icon="file"):
                    st.session_state.page = "Docs"
                    st.rerun()
                facade.LinkButton(
                    "GitHub",
                    url="https://github.com/itsdaniyalm/streamlit-facade",
                    variant="outline",
                    icon="external-link",
                    key="hero_github",
                )
    st.space(size="small")
    c1,c2,c3,c4 = st.columns([1,1,1,1])
    with c2:
        facade.IconCard(title="No build pipeline", description="Pure Python. No Node, no npm, no React. pip install and go. Infinite possiblities.", icon="terminal")
    with c3:
        facade.IconCard(title="Token system ", description="Define colors, fonts, and radius once. Every component inherits automatically.", icon="settings")
    st.space(size="small")
    c1,c2,c3,c4 = st.columns([1,1,1,1])
    with c2:
        facade.IconCard(title="Dark mode ", description="Presets ships with a matching dark variant. One toggle, instant switch.", icon="eye")
    with c3:
        facade.IconCard(title="LLM Ready", description="LLM-ready context file included. Drop it into Claude, ChatGPT, or Cursor and build faster.", icon="sparkle")
    st.space(size="large")
    with st.container(key="theme_section"):
        st.markdown("""
        <style>
            .st-key-theme_section {
                background: var(--primary) !important;
                border-radius: var(--radius);
                padding: 2rem;
            }
            .st-key-theme_section p,
            .st-key-theme_section h2,
            .st-key-theme_section strong {
                color: var(--primary-foreground) !important;
            }
        </style>
        """, unsafe_allow_html=True)

        st.space(size="medium")
        c1,c2,c3,c4 = st.columns([1,2,2,1], vertical_alignment="center")
        with c2:
            st.markdown("## One call. Every component.")
            st.markdown(":color[Facade gives you a proper design token system. Define your colors, fonts, and border radius once and component, button, card, alert, badge, input picks them up automatically.]{foreground='white'}")
            st.markdown(":color[Choose from 11 built-in presets or override any individual token to match your brand exactly. No CSS files, no config, no boilerplate!]{foreground='white'}")
            st.markdown("**Tokens**")
            with st.container(horizontal=True, gap="xxsmall"):
                facade.Badge("primary",    bg_color="var(--primary-foreground)", text_color="var(--primary)")
                facade.Badge("background", bg_color="var(--primary-foreground)", text_color="var(--primary)")
                facade.Badge("font-sans",  bg_color="var(--primary-foreground)", text_color="var(--primary)")
                facade.Badge("radius",     bg_color="var(--primary-foreground)", text_color="var(--primary)")
                facade.Badge("chrome",     bg_color="var(--primary-foreground)", text_color="var(--primary)")
        with c3:
            with st.container(border=True):
                st.code("""facade.theme.apply(
                    preset="carbon-sage",
                    base="light",
                    primary="#8FAF3D",
                    primary_foreground="#FFFFFF",
                    background="#F7F7F5",
                    foreground="#1C1917",
                    muted="#EFEFEB",
                    muted_foreground="#78716C",
                    border="#D9D9C8",
                    destructive="#EF4444",
                    chrome_background="#2C2C2C",
                    chrome_foreground="#F5F5F0",
                    chrome_border="#3A3A36",
                    font_sans="DM Sans",
                    font_mono="JetBrains Mono",
                    font_link="https://fonts.googleapis.com/...",
                    radius="lg",
                )""", language="python")
        st.space(size="medium")
    st.space(size="medium")
    st.markdown("## Presets", text_alignment="center")
    st.markdown("11 built-in presets, each with a light and dark variant.", text_alignment="center")
    st.space(size="medium")
    presets = [
        ("carbon-sage",      "#8FAF3D", "#F7F7F5"),
        ("default",          "#1059A0", "#FFFFFF"),
        ("minimal",          "#18181B", "#FAFAFA"),
        ("warm",             "#D97706", "#FFFBF0"),
        ("carbon-amber",     "#F59E0B", "#1C1917"),
        ("burgundy",         "#9B1D42", "#FAF7F5"),
        ("carbon-light",     "#84CC16", "#FFFFFF"),
        ("carbon-dark",      "#84CC16", "#0A0A08"),
        ("carbon-sage-dark", "#8FAF3D", "#1A1A16"),
        ("dark",             "#3B82F6", "#0F172A"),
        ("default-dark",     "#1059A0", "#0F172A"),
    ]

    cols = st.columns(11, gap="small")
    for i, (name, primary, bg) in enumerate(presets):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align:center;font-family:var(--font-sans);">
                <div style="width:2.5rem;height:2.5rem;background:{primary};border-radius:50%;margin:0 auto 0.5rem;border:1px solid rgba(0,0,0,0.1);"></div>
                <div style="font-size:0.7rem;font-weight:600;color:var(--foreground);">{name}</div>
            </div>""", unsafe_allow_html=True)
    st.space(size="large")
    st.markdown("## Components at a glance", text_alignment="center")
    st.markdown("20+ components, all themed automatically.", text_alignment="center")
    st.space(size="large")
    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        st.markdown("**Buttons**")
        with st.container(horizontal=True, gap="xxsmall"):
            facade.Button("Default", variant="default",     key="strip_btn1", size="sm")
            facade.Button("Outline", variant="outline",     key="strip_btn2", size="sm")
        with st.container(horizontal=True, gap="xxsmall"):
            facade.Button("Ghost",   variant="ghost",       key="strip_btn3", size="sm")
            facade.Button("Danger",  variant="destructive", key="strip_btn4", size="sm")
        st.space(size="small")
        st.markdown("**Badges**")
        with st.container(horizontal=True, gap="xxsmall"):
            facade.Badge("Default")
            facade.Badge("Outline", variant="outline")
            facade.Badge("Muted",   variant="muted")
        with st.container(horizontal=True, gap="xxsmall"):
            facade.Badge("Success", variant="success")
            facade.Badge("Warning", variant="warning")
            facade.Badge("Error",   variant="error")
            
    with c2:
        st.markdown("**Alerts**")
        facade.Alert("Success message", variant="success")
        facade.Alert("Warning message", variant="warning")
        facade.Alert("Error message",   variant="error")
        facade.Alert("Info message",    variant="info")
    with c3:
        st.markdown("**Metrics**")
        facade.Metric(label="Revenue", value="$24,500", delta="12%")
        st.space("xxsmall")
        facade.Metric(label="Churn",   value="3.2%",    delta="-0.5%")
    with c4:
        st.markdown("**Input**")
        facade.Input(placeholder="Type something...", key="strip_inp1")
        st.space(size="xsmall")
        st.markdown("**Select**")
        facade.Select(options=["Option A", "Option B", "Option C"], key="strip_sel1")
        st.space(size="xsmall")
        c1, c2 = st.columns([1,1], gap="xxsmall")
        with c1:
            st.markdown("**Toggle**")
            facade.Toggle("Enable notifications", key="strip_tog1")
            facade.Toggle("Dark mode", value=True, key="strip_tog2")
        with c2:
            st.markdown("**Radio**")
            facade.Radio(options=["Free", "Pro"], label="Plan", key="strip_rad1")
    st.space(size="large")
    facade.Separator()
    st.space(size="large")
    with st.container(key="footer_section"):
        f1, f2, f3 = st.columns([2, 3, 2], vertical_alignment="center")
        with f1:
            st.image("assets/mark.png", width=60)
            st.markdown("<p style='color:var(--primary-foreground);margin:0;'>streamlit but different.</p>", unsafe_allow_html=True)
        with f2:
            st.markdown("<p style='color:var(--primary-foreground);text-align:center;'>Built with ❤️ using facade · MIT License</p>", unsafe_allow_html=True)
        with f3:
            with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
                facade.LinkButton("GitHub", url="https://github.com/itsdaniyalm/streamlit-facade", variant="ghost", icon="external-link", key="footer_github")
                facade.LinkButton("PyPI",   url="https://pypi.org/project/streamlit-facade",       variant="ghost", icon="link",          key="footer_pypi")

##### Docs

elif st.session_state.page == "Docs":

    if facade.Button("Home", variant="ghost", icon="arrow-left", key="docs_back"):
        st.session_state.page = "Home"
        st.rerun()

    st.markdown("# Docs")
    st.markdown("Everything you need to build with streamlit-facade.")
    facade.Separator()

    (
        tab_gs, tab_comp, tab_theme, tab_icons, tab_changelog, tab_llm
    ) = facade.Tabs(["Getting Started", "Components", "Theme", "Icons", "Changelog", "LLM Context"])

    # ════════════════════════════════════════════════════════
    #  GETTING STARTED
    # ════════════════════════════════════════════════════════
    with tab_gs:
        st.markdown("### Install")
        st.code("pip install streamlit-facade", language="bash")
        facade.Alert("Requires Python 3.8+ and Streamlit 1.35.0+", variant="info", title="Requirements")
        st.markdown("### Quick start")
        prev_col, code_col = st.columns([1, 1], gap="large")
        with code_col:
            st.code("""import streamlit as st
import facade

facade.theme.apply(
    preset="carbon-sage",
    font_sans="DM Sans",
    font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",
    radius="lg",
)

facade.Alert("Welcome to facade!", variant="success", title="Hello")
facade.Button("Get started", icon="arrow-right", icon_position="right")
facade.Card(title="facade", description="streamlit but different")
""", language="python")
        with prev_col:
            with st.container(border=True):
                facade.Alert("Welcome to facade!", variant="success", title="Hello")
                facade.Button("Get started", icon="arrow-right", icon_position="right", key="gs_btn1")
                facade.Card(title="facade", description="streamlit but different")

    # ════════════════════════════════════════════════════════
    #  COMPONENTS
    # ════════════════════════════════════════════════════════
    with tab_comp:
        st.markdown("### Components")
        st.markdown("Every component is themed automatically via your design tokens.")
        facade.Separator()

        (
            ctab_button, ctab_linkbutton, ctab_input, ctab_select, ctab_textarea,
            ctab_checkbox, ctab_radio, ctab_toggle, ctab_slider, ctab_datepicker,
            ctab_card, ctab_iconcard, ctab_styledcontainer, ctab_alert, ctab_badge, ctab_metric,
            ctab_progress, ctab_spinner, ctab_toast, ctab_tabs, ctab_accordion
        ) = facade.Tabs([
            "Button", "LinkButton", "Input", "Select", "Textarea",
            "Checkbox", "Radio", "Toggle", "Slider", "DatePicker",
            "Card", "IconCard", "StyledContainer", "Alert", "Badge", "Metric",
            "Progress", "Spinner", "Toast", "Tabs", "Accordion"
        ])

        with ctab_button:
            st.markdown("#### Button")
            st.markdown("Themed button with variants, sizes, and icons.")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Button("Default",     variant="default",     key="doc_btn1")
                    facade.Button("Outline",     variant="outline",     key="doc_btn2")
                    facade.Button("Ghost",       variant="ghost",       key="doc_btn3")
                    facade.Button("Destructive", variant="destructive", key="doc_btn4")
                    st.markdown("**Sizes**")
                    facade.Button("Small",  size="sm", key="doc_btn5")
                    facade.Button("Medium", size="md", key="doc_btn6")
                    facade.Button("Large",  size="lg", key="doc_btn7")
                    st.markdown("**Icons**")
                    facade.Button("Save",  icon="save",        key="doc_btn8")
                    facade.Button("Next",  icon="arrow-right", icon_position="right", key="doc_btn9")
            with code_col:
                st.code("""facade.Button("Default",     variant="default")
facade.Button("Outline",     variant="outline")
facade.Button("Ghost",       variant="ghost")
facade.Button("Destructive", variant="destructive")

# Sizes: sm | md | lg
facade.Button("Small",  size="sm")
facade.Button("Medium", size="md")
facade.Button("Large",  size="lg")

# Icons
facade.Button("Save", icon="save")
facade.Button("Next", icon="arrow-right", icon_position="right")

# Returns bool
if facade.Button("Click me", key="btn1"):
    st.write("Clicked!")""", language="python")

        with ctab_linkbutton:
            st.markdown("#### LinkButton")
            st.markdown("Themed link button that navigates to an external URL. Visually identical to Button.")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.LinkButton("GitHub", url="https://github.com/itsdaniyalm/streamlit-facade", variant="default", icon="external-link", key="doc_lb1")
                    facade.LinkButton("PyPI",   url="https://pypi.org/project/streamlit-facade",       variant="outline", icon="link",          key="doc_lb2")
                    facade.LinkButton("Ghost",  url="https://github.com/itsdaniyalm/streamlit-facade", variant="ghost",   icon="external-link", key="doc_lb3")
            with code_col:
                st.code("""facade.LinkButton(
    "GitHub",
    url="https://github.com/...",
    variant="outline",
    icon="external-link",
    key="btn_github",
)
# Same variants, sizes, icons as Button
# Does not return bool — navigates on click""", language="python")

        with ctab_input:
            st.markdown("#### Input")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    val = facade.Input(placeholder="Type something...", label="Your name", key="doc_inp1")
                    if val:
                        facade.Alert(f"Hello, {val}!", variant="success")
            with code_col:
                st.code("""val = facade.Input(
    label="Your name",
    placeholder="Type something...",
    key="inp1",
)""", language="python")

        with ctab_select:
            st.markdown("#### Select")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    choice = facade.Select(options=["Option A", "Option B", "Option C"], placeholder="Pick an option...", key="doc_sel1")
                    if choice:
                        facade.Alert(f"Selected: {choice}", variant="info")
            with code_col:
                st.code("""choice = facade.Select(
    options=["Option A", "Option B", "Option C"],
    placeholder="Pick an option...",
    key="sel1",
)""", language="python")

        with ctab_textarea:
            st.markdown("#### Textarea")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Textarea(label="Message",  placeholder="Write something...", key="doc_ta1")
                    facade.Textarea(label="Bio",       max_chars=280,                   key="doc_ta2")
            with code_col:
                st.code("""facade.Textarea(label="Message", placeholder="Write something...")
facade.Textarea(label="Bio",     max_chars=280)
facade.Textarea(label="Notes",   height=200)""", language="python")

        with ctab_checkbox:
            st.markdown("#### Checkbox")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    c1 = facade.Checkbox("Accept terms and conditions", key="doc_chk1")
                    facade.Checkbox("Subscribe to newsletter", value=True, key="doc_chk2")
                    facade.Checkbox("Disabled option", disabled=True,     key="doc_chk3")
                    if c1:
                        facade.Alert("Terms accepted!", variant="success")
            with code_col:
                st.code("""facade.Checkbox("Accept terms", key="chk1")
facade.Checkbox("Subscribe",  value=True,    key="chk2")
facade.Checkbox("Disabled",   disabled=True, key="chk3")""", language="python")

        with ctab_radio:
            st.markdown("#### Radio")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    plan = facade.Radio(options=["Free", "Pro", "Enterprise"], label="Select plan", key="doc_rad1")
                    if plan == "Pro":
                        facade.Alert("You are on the Pro plan!", variant="success")
                    facade.Radio(options=["S", "M", "L"], label="Size", horizontal=True, key="doc_rad2")
            with code_col:
                st.code("""facade.Radio(
    options=["Free", "Pro", "Enterprise"],
    label="Select plan",
    key="radio1",
)
# Horizontal layout
facade.Radio(
    options=["S", "M", "L"],
    label="Size",
    horizontal=True,
    key="radio2",
)""", language="python")

        with ctab_toggle:
            st.markdown("#### Toggle")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    notifs = facade.Toggle("Enable notifications", key="doc_tog1")
                    facade.Toggle("Dark mode",  value=True,    key="doc_tog2")
                    facade.Toggle("Disabled",   disabled=True, key="doc_tog3")
                    if notifs:
                        facade.Alert("Notifications enabled.", variant="success")
            with code_col:
                st.code("""facade.Toggle("Enable notifications", key="tog1")
facade.Toggle("Dark mode",  value=True,    key="tog2")
facade.Toggle("Disabled",   disabled=True, key="tog3")""", language="python")

        with ctab_slider:
            st.markdown("#### Slider")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    vol = facade.Slider("Volume", min_value=0, max_value=100, value=50, key="doc_sl1")
                    st.caption(f"Volume: {vol}")
                    price = facade.Slider("Price range", min_value=0, max_value=1000, value=(100, 500), step=50, key="doc_sl2")
                    st.caption(f"${price[0]} – ${price[1]}")
            with code_col:
                st.code("""vol = facade.Slider("Volume", min_value=0, max_value=100, value=50)

# Range slider
price = facade.Slider(
    "Price range",
    min_value=0, max_value=1000,
    value=(100, 500), step=50,
)""", language="python")

        with ctab_datepicker:
            import datetime
            st.markdown("#### DatePicker")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    d = facade.DatePicker(label="Select date", key="doc_dp1")
                    if d: st.caption(f"Selected: {d}")
                    facade.DatePicker(label="With range",
                        min_value=datetime.date(2024, 1, 1),
                        max_value=datetime.date(2026, 12, 31),
                        key="doc_dp2")
                    facade.DatePicker(label="Disabled", disabled=True, key="doc_dp3")
            with code_col:
                st.code("""import datetime
facade.DatePicker(label="Select date", key="dp1")
facade.DatePicker(
    label="With range",
    min_value=datetime.date(2024, 1, 1),
    max_value=datetime.date(2026, 12, 31),
    key="dp2",
)
facade.DatePicker(label="Disabled", disabled=True, key="dp3")""", language="python")

        with ctab_card:
            st.markdown("#### Card")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Card(title="Card Title", description="Supporting description text goes here.")
                    facade.Card(title="Title only")
            with code_col:
                st.code("""facade.Card(
    title="Card Title",
    description="Supporting description text.",
)
facade.Card(title="Title only")""", language="python")

        with ctab_iconcard:
            st.markdown("#### IconCard")
            st.markdown("Card with a leading Lucide icon above the title.")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.IconCard(title="No build pipeline", description="Pure Python. No Node, no npm.", icon="terminal")
                    facade.IconCard(title="Token system", description="Define once, every component inherits.", icon="settings")
            with code_col:
                st.code("""facade.IconCard(
    title="No build pipeline",
    description="Pure Python. No Node, no npm.",
    icon="terminal",       # facade icon name
    icon_size=24,          # optional, default 24
)""", language="python")

        with ctab_styledcontainer:
            st.markdown("#### StyledContainer")
            st.markdown("A styled `st.container()` wrapper with configurable borders, background, and radius. Use it to group any Streamlit components inside a visually distinct card.")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    with facade.StyledContainer(border="top", border_color="#e05252", border_width="3px", key="doc_sc1"):
                        facade.Badge("Critical", variant="error")
                        st.markdown("### $43.8M")
                        st.caption("493 patients")
                    with facade.StyledContainer(border="left", border_color="var(--primary)", border_width="4px", key="doc_sc2"):
                        facade.Badge("Info", variant="muted")
                        st.markdown("**Left accent border**")
                    with facade.StyledContainer(border="all", key="doc_sc3"):
                        st.markdown("**All sides — default border**")
            with code_col:
                st.code("""# Top accent border
with facade.StyledContainer(
    border="top",
    border_color="#e05252",
    border_width="3px",
    key="card1",
):
    facade.Badge("Critical", variant="error")
    st.markdown("### $43.8M")
    st.caption("493 patients")

# Left accent border
with facade.StyledContainer(
    border="left",
    border_color="var(--primary)",
    border_width="4px",
    key="card2",
):
    st.markdown("Left accent")

# border: "top" | "bottom" | "left" | "right" | "all" | "none"
# border_surround_color sets the other 3 sides (default: var(--border))
# key is required for CSS scoping""", language="python")

        with ctab_alert:
            st.markdown("#### Alert")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Alert("Changes saved successfully.", variant="success", title="Saved!")
                    facade.Alert("This action cannot be undone.", variant="warning")
                    facade.Alert("Failed to connect.", variant="error", title="Error")
                    facade.Alert("Your trial ends in 3 days.", variant="info")
            with code_col:
                st.code("""facade.Alert("Saved!",   variant="success", title="Done")
facade.Alert("Heads up", variant="warning")
facade.Alert("Failed",   variant="error",   title="Error")
facade.Alert("Info",     variant="info")
# variants: success | warning | error | info""", language="python")

        with ctab_badge:
            st.markdown("#### Badge")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Badge("Default")
                    facade.Badge("Success", variant="success")
                    facade.Badge("Warning", variant="warning")
                    facade.Badge("Error",   variant="error")
                    facade.Badge("Outline", variant="outline")
                    facade.Badge("Muted",   variant="muted")
                    st.markdown("**Custom colors**")
                    facade.Badge("Premium", bg_color="#7C3AED", text_color="#fff")
                    facade.Badge("Beta", bg_color="#FFF7ED", text_color="#C2410C", border_color="#FDBA74")
            with code_col:
                st.code("""facade.Badge("Default")
facade.Badge("Success", variant="success")
facade.Badge("Warning", variant="warning")
facade.Badge("Error",   variant="error")
facade.Badge("Outline", variant="outline")
facade.Badge("Muted",   variant="muted")

# Custom colors
facade.Badge("Premium", bg_color="#7C3AED", text_color="#fff")
facade.Badge("Beta",
    bg_color="#FFF7ED",
    text_color="#C2410C",
    border_color="#FDBA74",
)""", language="python")

        with ctab_metric:
            st.markdown("#### Metric")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Metric(label="Revenue", value="$24,500", delta="12%")
                    facade.Metric(label="Churn",   value="3.2%",    delta="-0.5%")
                    facade.Metric(label="Uptime",  value="99.9%",   delta_color="off")
            with code_col:
                st.code("""facade.Metric(label="Revenue", value="$24,500", delta="12%")
facade.Metric(label="Churn",   value="3.2%",    delta="-0.5%")
facade.Metric(label="Uptime",  value="99.9%",   delta_color="off")
# delta_color: "normal" | "inverse" | "off" """, language="python")

        with ctab_progress:
            st.markdown("#### Progress")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    facade.Progress(value=100, label="Complete")
                    facade.Progress(value=75,  label="Uploading...")
                    facade.Progress(value=45,  label="Processing...")
                    facade.Progress(value=10,  label="Starting...")
            with code_col:
                st.code("""facade.Progress(value=75,  label="Uploading...")
facade.Progress(value=100, label="Complete")""", language="python")

        with ctab_spinner:
            st.markdown("#### Spinner")
            import time
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    if facade.Button("Trigger spinner", icon="refresh", key="doc_spinner_btn"):
                        with facade.Spinner("Loading data..."):
                            time.sleep(2)
                        facade.Alert("Done loading!", variant="success")
            with code_col:
                st.code("""import time
if facade.Button("Load", icon="refresh"):
    with facade.Spinner("Loading data..."):
        time.sleep(2)
    facade.Alert("Done!", variant="success")""", language="python")

        with ctab_toast:
            st.markdown("#### Toast")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    tc1, tc2, tc3 = st.columns(3, gap="small")
                    with tc1:
                        if facade.Button("Check", icon="check", key="doc_toast1"):
                            facade.Toast("Saved successfully!", icon="check")
                    with tc2:
                        if facade.Button("Info",  icon="info",  key="doc_toast2"):
                            facade.Toast("Here's some info.",   icon="info")
                    with tc3:
                        if facade.Button("Error", icon="error", key="doc_toast3"):
                            facade.Toast("Something went wrong.", icon="error")
            with code_col:
                st.code("""facade.Toast("Saved!",         icon="check")
facade.Toast("Info message",   icon="info")
facade.Toast("Error occurred", icon="error")""", language="python")

        with ctab_tabs:
            st.markdown("#### Tabs")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    t1, t2, t3 = facade.Tabs(["Overview", "Analytics", "Settings"])
                    with t1:
                        facade.Card(title="Overview", description="Tab content here.")
                    with t2:
                        facade.Metric(label="Sessions", value="12,400", delta="4%")
                    with t3:
                        facade.Toggle("Notifications", key="doc_tab_tog1")
                        facade.Button("Save", icon="save", key="doc_tab_btn1")
            with code_col:
                st.code("""tab1, tab2, tab3 = facade.Tabs(["Overview", "Analytics", "Settings"])
with tab1:
    facade.Card(title="Overview", description="Tab content.")
with tab2:
    facade.Metric(label="Sessions", value="12,400", delta="4%")
with tab3:
    facade.Toggle("Notifications", key="tog1")""", language="python")

        with ctab_accordion:
            st.markdown("#### Accordion")
            prev_col, code_col = st.columns([1, 1], gap="large")
            with prev_col:
                with st.container(border=True):
                    with facade.Accordion("Account details", expanded=True):
                        facade.Input(label="Full name", placeholder="John Doe", key="doc_ac_inp1")
                    with facade.Accordion("Notifications", icon="bell"):
                        facade.Toggle("Email notifications", key="doc_ac_tog1")
                    with facade.Accordion("Danger zone", icon="error"):
                        facade.Alert("Irreversible action.", variant="warning")
                        facade.Button("Delete", variant="destructive", icon="trash", key="doc_ac_btn1")
            with code_col:
                st.code("""with facade.Accordion("Account details", expanded=True):
    facade.Input(label="Full name", key="inp1")

with facade.Accordion("Notifications", icon="bell"):
    facade.Toggle("Email notifications", key="tog1")

with facade.Accordion("Danger zone", icon="error"):
    facade.Button("Delete", variant="destructive", icon="trash")""", language="python")

    # ════════════════════════════════════════════════════════
    #  THEME
    # ════════════════════════════════════════════════════════
    with tab_theme:
        st.markdown("### theme.apply()")
        st.markdown("One call sets your entire design token system. Every component inherits automatically.")
        st.code("""facade.theme.apply(
    preset="carbon-sage",         # built-in preset name
    base="light",                 # "light" | "dark"

    # Color tokens
    primary="#8FAF3D",
    primary_foreground="#FFFFFF",
    background="#F7F7F5",
    foreground="#1C1917",
    muted="#EFEFEB",
    muted_foreground="#78716C",
    border="#D9D9C8",
    destructive="#EF4444",

    # Chrome tokens (sidebar + topbar)
    chrome_background="#2C2C2C",
    chrome_foreground="#F5F5F0",
    chrome_border="#3A3A36",

    # Typography
    font_sans="DM Sans",
    font_mono="JetBrains Mono",
    font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",

    # Radius: xxs | sm | md | lg | xl
    radius="lg",
)""", language="python")

        facade.Separator()
        st.markdown("### Built-in presets")

        presets_info = [
            ("default",          "Classic blue, professional",        "#1059A0"),
            ("default-dark",     "Deep navy dark mode",               "#1059A0"),
            ("minimal",          "Near-black, tight radius",          "#18181B"),
            ("warm",             "Amber accent, warm cream",          "#D97706"),
            ("dark",             "Blue accent, dark slate",           "#3B82F6"),
            ("carbon-sage",      "Sage green, warm chalk",            "#8FAF3D"),
            ("carbon-sage-dark", "Sage green, warm carbon dark",      "#8FAF3D"),
            ("carbon-light",     "Electric lime, warm white",         "#84CC16"),
            ("carbon-dark",      "Electric lime, pure dark",          "#84CC16"),
            ("carbon-amber",     "Amber accent, warm carbon",         "#F59E0B"),
            ("burgundy",         "Deep burgundy, warm neutral",       "#9B1D42"),
        ]

        for name, desc, primary in presets_info:
            c1, c2, c3 = st.columns([0.05, 0.25, 1])
            with c1:
                st.markdown(f"<div style='width:1.25rem;height:1.25rem;background:{primary};border-radius:50%;margin-top:0.3rem;border:1px solid rgba(0,0,0,0.1);'></div>", unsafe_allow_html=True)
            with c2:
                facade.Badge(name, variant="outline")
            with c3:
                st.markdown(f"<span style='font-family:var(--font-sans);font-size:0.875rem;color:var(--muted-foreground)'>{desc}</span>", unsafe_allow_html=True)

        facade.Separator()
        st.markdown("### Radius scale")
        radii = [("xxs", "0.125rem"), ("sm", "0.25rem"), ("md", "0.5rem"), ("lg", "0.75rem"), ("xl", "1rem")]
        rc = st.columns(5, gap="small")
        for col, (name, val) in zip(rc, radii):
            with col:
                st.markdown(f"""
                <div style="background:var(--primary);color:var(--primary-foreground);padding:0.75rem;
                border-radius:{val};text-align:center;font-family:var(--font-sans);font-size:0.8rem;font-weight:500;">
                    {name}<br><span style="opacity:0.7;font-size:0.7rem">{val}</span>
                </div>""", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════
    #  ICONS
    # ════════════════════════════════════════════════════════
    with tab_icons:
        st.markdown("### Icons")
        st.markdown("facade ships **76 named icons** that work everywhere — buttons, alerts, accordions, toasts.")
        facade.Separator()

        st.markdown("### Usage")
        st.code("""# In Button (uses Material Symbols)
facade.Button("Save",   icon="save")
facade.Button("Delete", icon="trash",       variant="destructive")
facade.Button("Next",   icon="arrow-right", icon_position="right")

# In Accordion, Toast, Alert — same name
with facade.Accordion("Notifications", icon="bell"):
    ...
facade.Toast("Saved!", icon="check")

# Standalone Lucide SVG for custom HTML
from facade.lucide import icon_html
svg = icon_html("circle-check", size=16, color="var(--primary)")

# List all 76 names
facade.icon_names()""", language="python")

        facade.Alert(
            "Button icons use Material Symbols (native Streamlit). HTML component icons use Lucide SVGs. facade handles the translation — you always use the same name.",
            variant="info",
            title="How it works",
        )

        facade.Separator()
        st.markdown("### Icon registry")
        icons = facade.icon_names()
        cols_per_row = 6
        rows = [icons[i:i+cols_per_row] for i in range(0, len(icons), cols_per_row)]
        for row in rows:
            cols = st.columns(cols_per_row, gap="small")
            for col, name in zip(cols, row):
                with col:
                    facade.Badge(name, variant="outline")

    # ════════════════════════════════════════════════════════
    #  CHANGELOG
    # ════════════════════════════════════════════════════════
    with facade.Accordion("v0.1.5 — Latest", expanded=True, icon="check"):
            facade.Badge("Latest", variant="success")
            st.markdown("""
**Fixed**
- All component surfaces (`Card`, `IconCard`, `Input`, `Textarea`, `Select`, `Checkbox`, `Radio`, `DatePicker`, `Accordion`) now correctly use `--muted` token instead of `--background` — enables proper visual hierarchy when page and component backgrounds differ
- `StyledContainer` default background changed from `--background` to `--muted`

**Improved**
- `Button` padding reduced across all sizes for a tighter, more refined look
- `Button` forced `min-width` removed — icon-only buttons are now compact
            """)
        with facade.Accordion("v0.1.4", icon="check"):
            facade.Badge("v0.1.4", variant="muted")
            st.markdown("""
**New**
- `facade.StyledContainer` — styled `st.container()` wrapper with configurable accent borders (`top`, `bottom`, `left`, `right`, `all`, `none`), border color, border width, surround border color, background, and radius. `key` is required for CSS scoping.
            """)
            
    with tab_changelog:
        st.markdown("### Changelog")
        st.markdown("All notable changes to streamlit-facade.")
        facade.Separator()

        with facade.Accordion("v0.1.4 — Latest", expanded=True, icon="check"):
            facade.Badge("Latest", variant="success")
            st.markdown("""
**New**
- `facade.StyledContainer` — styled `st.container()` wrapper with configurable accent borders (`top`, `bottom`, `left`, `right`, `all`, `none`), border color, border width, surround border color, background, and radius. `key` is required for CSS scoping.
            """)

        with facade.Accordion("v0.1.3", icon="check"):
            facade.Badge("v0.1.3", variant="muted")
            st.markdown("""
**Fixed**
- Select component label collapsing — label now renders correctly when provided
            """)

        with facade.Accordion("v0.1.2", icon="check"):
            facade.Badge("v0.1.2", variant="muted")
            st.markdown("""
**New**
- `facade.IconCard` — card with a leading Lucide icon above the title. Accepts `icon`, `icon_size`, `title`, `description`.
- `"zap"` added to icon registry → `("zap", "bolt")`
            """)

        with facade.Accordion("v0.1.1", icon="check"):
            facade.Badge("v0.1.1", variant="muted")
            st.markdown("""
**New**
- `facade.LinkButton` — themed link button that navigates to external URLs. Same variants, sizes, and icons as `Button`.

**Fixed**
- README preset list corrected — removed internal `daniyal` preset, added `burgundy`
- Icon count clarified — 76 named shortcuts in registry, full Lucide (1500+) via `facade.Icon()`
            """)

        with facade.Accordion("v0.1.0 — Initial release", icon="sparkle"):
            facade.Badge("Initial", variant="muted")
            st.markdown("""
**Components**
- `Button`, `Input`, `Select`, `Textarea`, `Checkbox`, `Radio`, `Toggle`, `Slider`, `DatePicker`
- `Card`, `Alert`, `Badge`, `Metric`, `Separator`, `Progress`, `Spinner`, `Toast`
- `Tabs`, `Accordion`, `Sidebar`, `TopBar`

**Theme system**
- `facade.theme.apply()` with full token override support
- 11 built-in presets with light/dark variants
- CSS variable injection — all components inherit tokens automatically

**Icons**
- 76 named icons in unified registry
- `facade.icon_names()` to list all available names
            """)

    # ════════════════════════════════════════════════════════
    #  LLM CONTEXT
    # ════════════════════════════════════════════════════════
    with tab_llm:
        st.markdown("### LLM Context")
        st.markdown(
            "facade ships a ready-made context file for AI assistants. "
            "Drop it into Claude, ChatGPT, Cursor, or any LLM and start building immediately — "
            "no need to explain the API from scratch."
        )
        facade.Separator()

        facade.Alert(
            "The context file includes the full API reference, all component signatures, theme tokens, icon names, and usage patterns.",
            variant="info",
            title="What's included",
        )

        st.markdown("### How to use")
        st.markdown("""
1. Download the context file below
2. In **Claude** — add it to a Project as a knowledge file
3. In **ChatGPT** — attach it at the start of a conversation
4. In **Cursor** — add it to `.cursor/rules` or attach in chat
5. Start prompting — the LLM will know the full facade API
        """)

        facade.LinkButton(
            "Download context file",
            url="https://raw.githubusercontent.com/itsdaniyalm/streamlit-facade/main/CONTEXT.md",
            variant="default",
            icon="download",
            key="llm_download",
        )
