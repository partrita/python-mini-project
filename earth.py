import numpy as np
from netCDF4 import Dataset


def Etopo(lon_area, lat_area, resolution):
    """Read ETOPO1 topography data and select the requested region."""
    # Original resolution is 0.0167 degrees.
    data = Dataset("ETOPO1_Ice_g_gdal.grd", "r")

    lon_range = data.variables["x_range"][:]
    lat_range = data.variables["y_range"][:]
    spacing = data.variables["spacing"][:]
    dimension = data.variables["dimension"][:]
    z = data.variables["z"][:]
    lon_num = dimension[0]
    lat_num = dimension[1]

    lon_input = np.zeros(lon_num)
    lat_input = np.zeros(lat_num)
    for i in range(lon_num):
        lon_input[i] = lon_range[0] + i * spacing[0]
    for i in range(lat_num):
        lat_input[i] = lat_range[0] + i * spacing[1]

    lon, lat = np.meshgrid(lon_input, lat_input)
    topo = np.reshape(z, (lat_num, lon_num))

    if (resolution < spacing[0]) | (resolution < spacing[1]):
        print("Set the highest resolution")
    else:
        skip = int(resolution / spacing[0])
        lon = lon[::skip, ::skip]
        lat = lat[::skip, ::skip]
        topo = topo[::skip, ::skip]

    topo = topo[::-1]

    range1 = np.where((lon >= lon_area[0]) & (lon <= lon_area[1]))
    lon = lon[range1]
    lat = lat[range1]
    topo = topo[range1]
    range2 = np.where((lat >= lat_area[0]) & (lat <= lat_area[1]))
    lon = lon[range2]
    lat = lat[range2]
    topo = topo[range2]

    lon_num = len(np.unique(lon))
    lat_num = len(np.unique(lat))
    lon = np.reshape(lon, (lat_num, lon_num))
    lat = np.reshape(lat, (lat_num, lon_num))
    topo = np.reshape(topo, (lat_num, lon_num))

    data.close()
    return lon, lat, topo


def degree2radians(degree):
    """Convert degrees to radians."""
    return degree * np.pi / 180


def mapping_map_to_sphere(lon, lat, radius=1):
    """Map longitude and latitude points onto a sphere of the given radius."""
    lon = np.array(lon, dtype=np.float64)
    lat = np.array(lat, dtype=np.float64)
    lon = degree2radians(lon)
    lat = degree2radians(lat)
    xs = radius * np.cos(lon) * np.cos(lat)
    ys = radius * np.sin(lon) * np.cos(lat)
    zs = radius * np.sin(lat)
    return xs, ys, zs


def main():
    """Generate a 3D Plotly visualization of Earth topography."""
    resolution = 0.8
    lon_area = [-180.0, 180.0]
    lat_area = [-90.0, 90.0]

    lon_topo, lat_topo, topo = Etopo(lon_area, lat_area, resolution)
    xs, ys, zs = mapping_map_to_sphere(lon_topo, lat_topo)

    ctopo = [
        [0, "rgb(0, 0, 70)"],
        [0.2, "rgb(0,90,150)"],
        [0.4, "rgb(150,180,230)"],
        [0.5, "rgb(210,230,250)"],
        [0.50001, "rgb(0,120,0)"],
        [0.57, "rgb(220,180,130)"],
        [0.65, "rgb(120,100,0)"],
        [0.75, "rgb(80,70,0)"],
        [0.9, "rgb(200,200,200)"],
        [1.0, "rgb(255,255,255)"],
    ]

    import plotly.graph_objs as go
    from plotly.offline import plot

    topo_sphere = dict(
        type="surface",
        x=xs,
        y=ys,
        z=zs,
        colorscale=ctopo,
        surfacecolor=topo,
        cmin=-8000,
        cmax=8000,
    )
    noaxis = dict(
        showbackground=False,
        showgrid=False,
        showline=False,
        showticklabels=False,
        ticks="",
        title="",
        zeroline=False,
    )

    layout = go.Layout(
        autosize=False,
        width=1200,
        height=800,
        title="EARTH AND NEARBY SPACE",
        titlefont=dict(family="Courier New", color="white"),
        showlegend=False,
        scene=dict(
            xaxis=noaxis,
            yaxis=noaxis,
            zaxis=noaxis,
            aspectmode="manual",
            aspectratio=go.layout.scene.Aspectratio(x=1, y=1, z=1),
        ),
        paper_bgcolor="dimgray",
        plot_bgcolor="dimgray",
    )

    fig = go.Figure(data=[topo_sphere], layout=layout)
    plot(fig, validate=False, filename="Earth.html", auto_open=True)


if __name__ == "__main__":
    main()
