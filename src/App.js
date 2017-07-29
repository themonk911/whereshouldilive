import React, { Component }  from 'react'
import { render } from 'react-dom'
import { Map, TileLayer, Marker, Popup, LayersControl, FeatureGroup, GeoJSON} from 'react-leaflet'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import boundary_json from './data/ACT-Division-Boundaries.json'
import {distance_to_police_departments} from './data/distance_to_police_departments.js'

class SimpleExample extends Component {

  constructor()
  {
    super();
    this.position =    [-35.325, 149.09];
    this.onEachFeature = this.onEachFeature.bind(this);
  }
  compute_intensity()
  {

  }
  onEachFeature(feature, layer) {    
    console.log("Here");
    layer.bindTooltip(feature.properties.division_name);    
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
                  <HeatmapLayer
                    points={distance_to_police_departments}
                    longitudeExtractor={m => m[0]}
                    latitudeExtractor={m => m[1]}
                    intensityExtractor={m => m[2]*this.props.intensity*100}
                  />
                </FeatureGroup>
              </LayersControl.Overlay>

              <LayersControl.Overlay name="Boundaries"
              fitBoundsOnLoad
              fitBoundsOnUpdate
              checked              
              onEachFeature={this.onEachFeature}
              >              
                <GeoJSON data={boundary_json} />
              </LayersControl.Overlay>
              </LayersControl>
          </Map>
        </div>
    );
  }

}

export default SimpleExample;
