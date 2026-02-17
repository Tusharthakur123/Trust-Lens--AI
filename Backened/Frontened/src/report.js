import React from "react";

function Report({ result }) {
  if (!result) return null;

  return (
    <div>
      <h2>AI Condition Report</h2>
      <p><strong>Damage Level:</strong> {result.damage_level}</p>
      <p><strong>Severity Score:</strong> {result.severity_score}</p>
      <p><strong>Fraud Score:</strong> {result.fraud_score}</p>
      <p><strong>Recommended Price:</strong> ₹{result.recommended_price}</p>
      <p><strong>Trust Score:</strong> {result.trust_score}/100</p>
      <p><strong>Explanation:</strong> {result.explanation}</p>
    </div>
  );
}

export default Report;
