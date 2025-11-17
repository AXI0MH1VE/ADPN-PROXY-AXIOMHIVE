
import plotly.graph_objects as go

# Define the comparison data
dimensions = [
    "Detection Method",
    "Zero-Day Capability",
    "False Positive Rate",
    "Response Time",
    "Adaptability",
    "Insider Threat Detection",
    "In-Memory Exploit Defense",
    "Lateral Movement Prevention",
    "Cost of Compromise",
    "Time to Detect (avg)"
]

legacy_values = [
    "Signature patterns",
    "0%",
    "High",
    ">1000ms",
    "Static",
    "Limited",
    "Minimal",
    "Reactive",
    "High",
    ">200 days"
]

adpn_values = [
    "Behavioral analysis",
    "95%+",
    "Low",
    "100-200ms",
    "Dynamic",
    "Advanced",
    "Comprehensive",
    "Proactive",
    "Low",
    "<1 hour"
]

# Create the table
fig = go.Figure(data=[go.Table(
    columnwidth=[2, 2, 2],
    header=dict(
        values=['<b>Dimension</b>', '<b>Legacy Signature-Based</b>', '<b>ADPN Adaptive</b>'],
        fill_color='#1FB8CD',
        align='left',
        font=dict(color='white', size=14),
        height=40
    ),
    cells=dict(
        values=[dimensions, legacy_values, adpn_values],
        fill_color=[['#F5F5F5', 'white']*5],
        align='left',
        font=dict(size=12),
        height=35
    )
)])

fig.update_layout(
    title="Legacy vs ADPN Defense Comparison"
)

# Save as PNG and SVG
fig.write_image("comparison_table.png")
fig.write_image("comparison_table.svg", format="svg")
