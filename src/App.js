import React, { Component }  from 'react'
import { render } from 'react-dom'
import { Map, TileLayer, Marker, Popup, LayersControl, FeatureGroup} from 'react-leaflet'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import { addressPoints } from './realworld.10000.js';

class SimpleExample extends Component {
  
  constructor()
  {
    super();
    this.position =    [50.05, -0.09];  
  }
 render() {
    return (      
      <Map center={this.position} zoom={13} >
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
                    fitBoundsOnLoad
                    fitBoundsOnUpdate
                    points={addressPoints}
                    longitudeExtractor={m => m[1]}
                    latitudeExtractor={m => m[0]}
                    intensityExtractor={m => parseFloat(m[2])}
                  />
                </FeatureGroup>
              </LayersControl.Overlay>
              <LayersControl.Overlay name="Marker" checked>
                <FeatureGroup color="purple">
                  <Marker position={this.position} >
                    <Popup>
                      <span>A pretty CSS3 popup.<br /> Easily customizable. </span>
                    </Popup>
                  </Marker>
                </FeatureGroup>
              </LayersControl.Overlay>
            </LayersControl>
          </Map>
    );
  }

}

export default SimpleExample;