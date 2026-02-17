import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar, PieChart, Pie, Cell } from 'recharts';

const catalystData = [
  { name: 'NiFe', overpotential: 0.25, currentDensity: 1.2 },
  { name: 'NiCo', overpotential: 0.22, currentDensity: 1.4 },
  { name: 'NiMo', overpotential: 0.19, currentDensity: 1.6 },
  { name: 'NiCr', overpotential: 0.21, currentDensity: 1.3 },
  { name: 'NiFeCo', overpotential: 0.18, currentDensity: 1.8 },
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

export default function Dashboard() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1 style={{ textAlign: 'center' }}>Quantum Catalyst Dashboard</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-around' }}>
        <div style={{ width: '45%', minWidth: '300px' }}>
          <h3>Overpotential by Catalyst</h3>
          <LineChart width={400} height={300} data={catalystData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="overpotential" stroke="#8884d8" activeDot={{ r: 8 }} />
          </LineChart>
        </div>
        <div style={{ width: '45%', minWidth: '300px' }}>
          <h3>Current Density</h3>
          <BarChart width={400} height={300} data={catalystData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="currentDensity" fill="#82ca9d" />
          </BarChart>
        </div>
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '40px' }}>
        <div>
          <h3>Composition Distribution</h3>
          <PieChart width={400} height={300}>
            <Pie
              data={catalystData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={(entry) => entry.name}
              outerRadius={80}
              fill="#8884d8"
              dataKey="currentDensity"
            >
              {catalystData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </div>
      </div>
    </div>
  );
}
