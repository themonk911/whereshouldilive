import React, { Component }  from 'react'
import { render } from 'react-dom'
import { Map, TileLayer, Marker, Popup, LayersControl, FeatureGroup, GeoJSON} from 'react-leaflet'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import boundary_json from './data/ACT-Division-Boundaries.json'
import {summary} from './data/expanded_summary.js'

class DataConnector extends Component {

  constructor()
  {
    super();
    this.position =    [-35.325, 149.09];
    this.compute_intensity = this.compute_intensity.bind(this);
  }
  compute_intensity(weight_array, intensity_array)
  {
    var magic_const = 10.0;
    // The slider passes in things in chunks of 10.
    // Need to divide by 10 to get back to normal.
    if (weight_array.length !== intensity_array.length)
    {
      return false;
    }
    var normaliser = weight_array.length;
    var sum = 0;
    for (var i=0; i<weight_array.length; i++)
    {
      sum += weight_array[i] * intensity_array[i] / magic_const;
    }
    if (isNaN(sum))
    {
        sum = normaliser;
    }
    if (normaliser > 0)
    {
        return sum/normaliser;
    }
    else
    {
        return sum;
    }
  }
  onEachFeature(feature, layer) {
    layer.bindTooltip(feature.properties.division_name);
  }
 render() {
    return (
    <div id="map">
      <Map center={this.position} zoom={11.2} >
            <LayersControl>
              <LayersControl.BaseLayer name="Base" checked>
                <TileLayer
                  url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
                  attribution="&copy; <a href=http://osm.org/copyright>OpenStreetMap</a> contributors"
                />
              </LayersControl.BaseLayer>

              <LayersControl.Overlay name="Summary" checked>
                <FeatureGroup color="red">
                  <HeatmapLayer
                    points={summary}
                    radius={1000}
                    blur={5000}
                    longitudeExtractor={m => m[1]}
                    latitudeExtractor={m => m[2]}
                    intensityExtractor={m => this.compute_intensity(
                      [m[3], m[4], m[5], m[6], m[7], m[8]],
                      [this.props.education_intensity, this.props.nature_intensity, this.props.health_intensity, this.props.housing_intensity, this.props.safety_intensity, this.props.transport_intensity]
                      )}
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

export default DataConnector;
