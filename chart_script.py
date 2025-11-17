
import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

# Define positions for elements
# External Entities
me_x, me_y = 1, 8
ho_x, ho_y = 9, 8

# Processes (circles)
p1_x, p1_y = 5, 7
p2_x, p2_y = 5, 4
p3_x, p3_y = 1, 4
p4_x, p4_y = 8, 4

# Data Stores (parallel lines)
d1_x, d1_y = 7.5, 6
d2_x, d2_y = 7.5, 2.5

# Helper function to draw circle
def add_circle(fig, x, y, r, text, color='#B3E5EC'):
    theta = np.linspace(0, 2*np.pi, 100)
    circle_x = x + r * np.cos(theta)
    circle_y = y + r * np.sin(theta)
    
    fig.add_trace(go.Scatter(
        x=circle_x, y=circle_y,
        fill='toself',
        fillcolor=color,
        line=dict(color='#13343B', width=2),
        mode='lines',
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig.add_annotation(
        x=x, y=y,
        text=text,
        showarrow=False,
        font=dict(size=9, color='#13343B'),
        align='center'
    )

# Helper function to draw rectangle (external entity)
def add_rectangle(fig, x, y, w, h, text, color='#B3E5EC'):
    fig.add_trace(go.Scatter(
        x=[x-w/2, x+w/2, x+w/2, x-w/2, x-w/2],
        y=[y-h/2, y-h/2, y+h/2, y+h/2, y-h/2],
        fill='toself',
        fillcolor=color,
        line=dict(color='#13343B', width=2),
        mode='lines',
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig.add_annotation(
        x=x, y=y,
        text=text,
        showarrow=False,
        font=dict(size=9, color='#13343B'),
        align='center'
    )

# Helper function to draw data store (parallel lines)
def add_datastore(fig, x, y, w, h, text, label, color='#A5D6A7'):
    # Top and bottom lines
    fig.add_trace(go.Scatter(
        x=[x-w/2, x+w/2],
        y=[y+h/2, y+h/2],
        line=dict(color='#13343B', width=2),
        mode='lines',
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig.add_trace(go.Scatter(
        x=[x-w/2, x+w/2],
        y=[y-h/2, y-h/2],
        line=dict(color='#13343B', width=2),
        mode='lines',
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Fill
    fig.add_trace(go.Scatter(
        x=[x-w/2, x+w/2, x+w/2, x-w/2, x-w/2],
        y=[y-h/2, y-h/2, y+h/2, y+h/2, y-h/2],
        fill='toself',
        fillcolor=color,
        line=dict(color='rgba(0,0,0,0)', width=0),
        mode='lines',
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig.add_annotation(
        x=x-w/2-0.3, y=y,
        text=f"<b>{label}</b>",
        showarrow=False,
        font=dict(size=9, color='#13343B'),
        align='right'
    )
    
    fig.add_annotation(
        x=x, y=y,
        text=text,
        showarrow=False,
        font=dict(size=8, color='#13343B'),
        align='center'
    )

# Helper function to draw arrow
def add_arrow(fig, x1, y1, x2, y2, text=''):
    fig.add_annotation(
        x=x2, y=y2,
        ax=x1, ay=y1,
        xref='x', yref='y',
        axref='x', ayref='y',
        text='',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='#13343B'
    )
    
    if text:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        fig.add_annotation(
            x=mid_x, y=mid_y,
            text=text,
            showarrow=False,
            font=dict(size=7, color='#13343B'),
            bgcolor='white',
            borderpad=2
        )

# Draw Trust Boundaries (dashed rectangles)
# Untrusted Operational Plane
fig.add_trace(go.Scatter(
    x=[0, 2.5, 2.5, 0, 0],
    y=[2.5, 2.5, 9, 9, 2.5],
    line=dict(color='#DB4545', width=2, dash='dash'),
    mode='lines',
    showlegend=False,
    hoverinfo='skip'
))

fig.add_annotation(
    x=1.25, y=8.7,
    text="<b>Untrusted Plane</b>",
    showarrow=False,
    font=dict(size=9, color='#DB4545')
)

# High-Trust Analysis Plane
fig.add_trace(go.Scatter(
    x=[3.5, 10, 10, 3.5, 3.5],
    y=[1.5, 1.5, 9, 9, 1.5],
    line=dict(color='#2E8B57', width=2, dash='dash'),
    mode='lines',
    showlegend=False,
    hoverinfo='skip'
))

fig.add_annotation(
    x=6.75, y=8.7,
    text="<b>High-Trust Plane</b>",
    showarrow=False,
    font=dict(size=9, color='#2E8B57')
)

# Draw External Entities
add_rectangle(fig, me_x, me_y, 1.2, 0.6, "Managed<br>Endpoint", '#FFCDD2')
add_rectangle(fig, ho_x, ho_y, 1.2, 0.6, "Human<br>Operator", '#FFCDD2')

# Draw Processes
add_circle(fig, p1_x, p1_y, 0.6, "1.0<br>Establish Self<br>Baseline", '#B3E5EC')
add_circle(fig, p2_x, p2_y, 0.6, "2.0<br>Monitor<br>Non-Self", '#B3E5EC')
add_circle(fig, p3_x, p3_y, 0.6, "3.0<br>Trigger<br>Response", '#B3E5EC')
add_circle(fig, p4_x, p4_y, 0.6, "4.0<br>Update<br>Memory", '#B3E5EC')

# Draw Data Stores
add_datastore(fig, d1_x, d1_y, 1.5, 0.5, "System<br>Baseline", "D1", '#A5D6A7')
add_datastore(fig, d2_x, d2_y, 1.5, 0.5, "Immunological<br>Memory", "D2", '#A5D6A7')

# Draw Data Flows
add_arrow(fig, me_x+0.6, me_y-0.1, p1_x-0.5, p1_y+0.2, 'Endpoint<br>Telemetry')
add_arrow(fig, me_x+0.4, me_y-0.3, p2_x-0.5, p2_y+0.5, 'Network<br>Flows')
add_arrow(fig, p1_x+0.5, p1_y-0.3, d1_x-0.75, d1_y+0.1, 'Store')
add_arrow(fig, d1_x-0.75, d1_y-0.1, p2_x+0.5, p2_y+0.3, 'Read')
add_arrow(fig, p2_x-0.5, p2_y-0.1, p3_x+0.6, p3_y, 'Anomaly Flag')
add_arrow(fig, p3_x+0.2, p3_y+0.5, me_x, me_y-0.3, 'Neutralize<br>Command')
add_arrow(fig, p2_x+0.5, p2_y-0.2, p4_x-0.3, p4_y+0.5, 'Update Data')
add_arrow(fig, p4_x, p4_y-0.6, d2_x-0.2, d2_y+0.25, 'Write')
add_arrow(fig, d2_x-0.5, d2_y, p2_x+0.6, p2_y-0.5, 'Read')
add_arrow(fig, ho_x-0.6, ho_y, p1_x+0.6, p1_y+0.1, 'Config')
add_arrow(fig, p4_x+0.5, p4_y+0.4, ho_x-0.3, ho_y-0.3, 'Reports')

# Update layout
fig.update_layout(
    title="ADPN Self/Non-Self Discrimination",
    xaxis=dict(range=[-0.5, 10.5], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[1, 9.5], showgrid=False, zeroline=False, visible=False),
    plot_bgcolor='white',
    showlegend=False
)

fig.update_xaxes(scaleanchor="y", scaleratio=1)

# Save the figure
fig.write_image('dfd_diagram.png')
fig.write_image('dfd_diagram.svg', format='svg')

print("DFD diagram saved successfully")
