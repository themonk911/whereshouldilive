import React, { Component }  from 'react'
import { render } from 'react-dom'
import { Map, TileLayer, Marker, Popup, LayersControl, FeatureGroup, GeoJSON} from 'react-leaflet'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import boundary_json from './data/ACT-Division-Boundaries.json'
import {distance_to_police_departments} from './data/distance_to_police_departments.js'
import {fitness_sites} from './data/fitness_sites.js'

class SimpleExample extends Component {

  constructor()
  {
    super();
    this.position =    [-35.325, 149.09];
    this.onEachFeature = this.onEachFeature.bind(this);    
  }
  compute_intensity(weight_array, intensity_array)
  {
    if (weight_array.length !== intensity_array.length)
    {
      return false;
    }
    var sum = 0;
    for (var i=0; i<weight_array.length; i++)
    {
      sum += weight_array[i] * intensity_array[i];
    }
    return sum;
  }
  onEachFeature(feature, layer) {    
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

              <LayersControl.Overlay name="Distance to Police Heatmap" checked>
                <FeatureGroup color="purple">                  
                  <HeatmapLayer
                    points={distance_to_police_departments}
                    longitudeExtractor={m => m[0]}
                    latitudeExtractor={m => m[1]}
                    intensityExtractor={m => m[2]*this.props.intensity}
                  />
                </FeatureGroup>
              </LayersControl.Overlay>

              <LayersControl.Overlay name="Fitness heatmap" checked>
                <FeatureGroup color="purple">                  
                  <HeatmapLayer
                    points={fitness_sites}
                    longitudeExtractor={m => m[0]}
                    latitudeExtractor={m => m[1]}
                    intensityExtractor={m => m[2]*this.props.intensity}
                    radius={50}                    
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
              </LayersControl>
          </Map>
        </div>
    );
  }

}

export default SimpleExample;
