import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_elk_diagram_mpl():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 8)
    ax.axis('off')

    # Colors
    color_orange = '#ff9900'
    color_blue = '#007acc'
    color_darkblue = '#1a237e'
    color_purple = '#7b1fa2'
    color_grafana = '#f57f17'
    text_white = '#ffffff'

    # Helper to draw box
    def draw_box(x, y, width, height, color, label, fontsize=10):
        # Draw shadow
        shadow = patches.FancyBboxPatch((x+0.05, y-0.05), width, height, boxstyle="round,pad=0.1",
                                      linewidth=0, facecolor='gray', alpha=0.3)
        ax.add_patch(shadow)

        rect = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1",
                                      linewidth=1, edgecolor='none', facecolor=color)
        ax.add_patch(rect)
        ax.text(x + width/2, y + height/2, label, ha='center', va='center',
                color=text_white, fontsize=fontsize, fontweight='bold')
        return {
            'center': (x + width/2, y + height/2),
            'right': (x + width, y + height/2),
            'left': (x, y + height/2),
            'top': (x + width/2, y + height),
            'bottom': (x + width/2, y)
        }

    # === Equipment Layer (Left Column) ===
    equip_labels = [
        "MSSQL Database", "Windows Servers", "Cisco Network", "Active Directory", "Firewall / WAF"
    ]
    equip_y_start = 1.0
    equip_nodes = []

    for i, lbl in enumerate(equip_labels):
        y_pos = equip_y_start + i * 1.2
        node = draw_box(0.5, y_pos, 2.5, 0.8, color_orange, lbl)
        equip_nodes.append(node)

    # === Ingestion Layer (Center Left) ===
    ls_y = 3.5
    ls_node = draw_box(4.5, ls_y, 2.5, 1.2, color_blue, "Logstash Cluster\n(Normalization)", fontsize=11)

    # === Storage Layer (Center Right) ===
    es_node = draw_box(8.5, ls_y, 2.5, 1.2, color_darkblue, "Elasticsearch\n(Hot/Warm)", fontsize=11)

    # === Visualization Layer (Top Right) ===
    kib_node = draw_box(8.5, 6.0, 2.5, 1.0, color_grafana, "Kibana", fontsize=11)

    # === Dashboards (Far Right Column) ===
    dash_labels = ["Operations", "Identity Mgmt", "Traffic Ana.", "Threat Mon."]
    dash_nodes = []

    for i, lbl in enumerate(dash_labels):
        y_pos = 2.0 + i * 1.2
        node = draw_box(12.5, y_pos, 2.5, 0.8, color_purple, lbl)
        dash_nodes.append(node)

    # === Connections ===
    # Use standard arrows (arc3) which are robust against "no intersection" errors

    # 1. Equipment -> Logstash
    for eq in equip_nodes:
        ax.annotate("",
            xy=ls_node['left'], xycoords='data',
            xytext=eq['right'], textcoords='data',
            arrowprops=dict(arrowstyle="->", color="#555", lw=1.5, connectionstyle="arc3,rad=-0.1")
        )

    # 2. Logstash -> ES
    # Straight line usually fine, but if coordinates align perfectly, simple arrow is safest
    ax.annotate("",
            xy=es_node['left'], xycoords='data',
            xytext=ls_node['right'], textcoords='data',
            arrowprops=dict(arrowstyle="simple", color="#333", alpha=0.6)
        )

    # 3. ES -> Kibana
    ax.annotate("",
            xy=kib_node['bottom'], xycoords='data',
            xytext=es_node['top'], textcoords='data',
            arrowprops=dict(arrowstyle="simple", color="#333", alpha=0.6)
        )

    # 4. Kibana -> Dashboards
    for dash in dash_nodes:
        # Use arc3 for everything to be safe
        ax.annotate("",
            xy=dash['left'], xycoords='data',
            xytext=kib_node['right'], textcoords='data',
            arrowprops=dict(arrowstyle="->", color="purple", linestyle="dashed",
                            lw=1.5, connectionstyle="arc3,rad=0.2")
        )

    # === Titles ===
    title_y = 7.5
    ax.text(1.75, title_y, "Device Layer", fontsize=14, fontweight='bold', color='#444', ha='center')
    ax.text(5.75, title_y, "Ingestion", fontsize=14, fontweight='bold', color='#444', ha='center')
    ax.text(9.75, title_y, "Storage & Viz", fontsize=14, fontweight='bold', color='#444', ha='center')
    ax.text(13.75, title_y, "Dashboards", fontsize=14, fontweight='bold', color='#444', ha='center')

    # Draw separator lines (optional)
    ax.vlines(x=[3.5, 7.5, 11.5], ymin=0, ymax=7.8, colors='#ddd', linestyles='dashed')

    output_path = 'projects/01-walsin/images/walsin_architecture_hq.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated {output_path}")

if __name__ == '__main__':
    generate_elk_diagram_mpl()
