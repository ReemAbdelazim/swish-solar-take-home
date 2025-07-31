'use client';

import { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);

type SoilingEntry = {
  date: string;
  soiling_loss_percent: number;
};

export default function Home() {
  const [data, setData] = useState<SoilingEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch("http://localhost:8000/soiling")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch(() => {
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) return <p style={{ padding: "1rem" }}>Loading chart...</p>;
  if (error) return <p style={{ padding: "1rem", color: "red" }}>Failed to load data.</p>;

  const chartData = {
    labels: data.map((entry) => entry.date),
    datasets: [
      {
        label: "Soiling Loss (%)",
        data: data.map((entry) => entry.soiling_loss_percent),
        borderColor: "rgb(75, 192, 192)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        tension: 0.3,
      },
    ],
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Soiling Loss Over Time</h1>
      <Line data={chartData} />
    </div>
  );
}
