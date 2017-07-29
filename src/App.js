import React, { Component }  from 'react'
import { render } from 'react-dom'
import { Map, TileLayer, Marker, Popup } from 'react-leaflet'
import HeatmapLayer from 'react-leaflet-heatmap-layer';
import { addressPoints } from './realworld.10000.js';

class SimpleExample extends Component {

  render() {
    return (
      <div>
        <Map center={[0,0]} zoom={13}>
          <HeatmapLayer
            fitBoundsOnLoad
            fitBoundsOnUpdate
            points={addressPoints}
            longitudeExtractor={m => m[1]}
            latitudeExtractor={m => m[0]}
            intensityExtractor={m => parseFloat(m[2])} />
          <TileLayer
            url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
        </Map>
      </div>
    );
  }

}

export default SimpleExample;