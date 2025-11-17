
import plotly.graph_objects as go

# Comprehensive threat landscape statistics with all data points
categories = [
    'Zero-Days 2024',
    'Ransom Detect %',
    'Breach Cost $4.88M',
    'Breach Cost $5.08M',
    'Security Tgt %',
    'Malware Var (sec)',
    'Discovery (days)'
]

values = [
    75,        # Zero-days exploited in 2024
    99.65,     # Ransomware detection rate %
    4.88,      # Global breach cost 2024 in millions
    5.08,      # Breach cost 2025 in millions
    44,        # % zero-day exploits targeting security/networking
    15,        # Polymorphic malware new variant every 15 seconds
    208        # Average days between infection and discovery
]

# Use alternating colors from the brand palette
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', '#B4413C', '#964325']

# Create horizontal bar chart with all metrics
fig = go.Figure(data=[
    go.Bar(
        x=values,
        y=categories,
        orientation='h',
        marker=dict(color=colors),
        text=values,
        texttemplate='%{text}',
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Value: %{x}<extra></extra>'
    )
])

fig.update_layout(
    title='Threat Landscape Dashboard 2024',
    xaxis_title='Metric Value',
    yaxis_title='',
    showlegend=False
)

fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image('threat_dashboard.png')
fig.write_image('threat_dashboard.svg', format='svg')
