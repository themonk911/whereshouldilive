import React, { Component }  from 'react'
import { render } from 'react-dom'
import { Map, TileLayer, Marker, Popup, LayersControl, FeatureGroup, GeoJSON} from 'react-leaflet'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import { addressPoints } from './realworld.10000.js';
import boundary_json from './data/ACT-Division-Boundaries.json'
import division_json from './data/division_center.json'

class SimpleExample extends Component {

  constructor()
  {
    super();
    this.position =    [-35.325, 149.09];
  }
 render() {
    return (
    <div>
      <Map center={this.position} zoom={11} >
            <LayersControl>
              <LayersControl.BaseLayer name="Base" checked>
                <TileLayer
                  url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
                  attribution="&copy; <a href=http://osm.org/copyright>OpenStreetMap</a> contributors"
                />
              </LayersControl.BaseLayer>

              <LayersControl.Overlay name="Heatmap" checked>
                <FeatureGroup color="purple">
                  <Marker position={this.position} >
                    <Popup>
                      <span>A pretty CSS3 popup.<br /> Easily customizable. </span>
                    </Popup>
                  </Marker>
                  <HeatmapLayer

                    points={addressPoints}
                    longitudeExtractor={m => m[1]}
                    latitudeExtractor={m => m[0]}
                    intensityExtractor={m => parseFloat(m[2])*this.props.intensity}

                  />
                </FeatureGroup>
              </LayersControl.Overlay>

              <LayersControl.Overlay name="Boundaries"
              fitBoundsOnLoad
              fitBoundsOnUpdate
              checked
              >
                <GeoJSON data={boundary_json} />
              </LayersControl.Overlay>

              <LayersControl.Overlay name="Division Center"
              checked
              >
                <GeoJSON data={division_json} />
              </LayersControl.Overlay>

            </LayersControl>
          </Map>
        </div>
    );
  }

}

export default SimpleExample;
