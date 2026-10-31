import { useState } from "react";
import UploadBox from "./components/UploadBox";
import ProposalViewer from "./components/ProposalViewer";
import "./App.css";

function App() {
  const [proposal, setProposal] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [similarProjects, setSimilarProjects] = useState([]);

  const [docxDownload, setDocxDownload] = useState("");
  const [pdfDownload, setPdfDownload] = useState("");

  return (
    <div
      style={{
        maxWidth: "1200px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Segoe UI, sans-serif",
      }}
    >
      {/* Header */}

      <div style={{ textAlign: "center", marginBottom: "40px" }}>
        <h1
          style={{
            fontSize: "42px",
            color: "#1e40af",
            marginBottom: "10px",
          }}
        >
          🤖 AI Proposal Automation
        </h1>

        <p
          style={{
            fontSize: "18px",
            color: "#64748b",
            maxWidth: "800px",
            margin: "0 auto",
            lineHeight: "1.7",
          }}
        >
          Upload a <strong>Software Requirement PDF</strong>. The system
          validates the document using AI, analyzes the requirements,
          retrieves similar projects using RAG, and generates a professional
          proposal in DOCX and PDF formats.
        </p>
      </div>

      {/* Upload */}

      <UploadBox
        setProposal={setProposal}
        setAnalysis={setAnalysis}
        setSimilarProjects={setSimilarProjects}
        setDocxDownload={setDocxDownload}
        setPdfDownload={setPdfDownload}
      />

      {/* Empty State */}

      {!proposal && (
        <div
          style={{
            marginTop: "40px",
            background: "#f8fafc",
            padding: "35px",
            borderRadius: "16px",
            textAlign: "center",
            border: "1px solid #e2e8f0",
          }}
        >
          <h2 style={{ color: "#1e293b" }}>
            📄 Upload Your Requirement Document
          </h2>

          <p
            style={{
              color: "#64748b",
              marginTop: "15px",
              lineHeight: "1.8",
            }}
          >
            Supported Documents
            <br />
            ✔ Client Requirement
            <br />
            ✔ Software Requirement Specification (SRS)
            <br />
            ✔ Business Requirement Document (BRD)
            <br />
            <br />
            Unsupported Documents
            <br />
            ✖ Resume
            <br />
            ✖ Certificate
            <br />
            ✖ Business Proposal
          </p>
        </div>
      )}

      {/* Proposal */}

      <ProposalViewer
        proposal={proposal}
        analysis={analysis}
        similarProjects={similarProjects}
        docxDownload={docxDownload}
        pdfDownload={pdfDownload}
      />

      {/* Footer */}

      <footer
        style={{
          marginTop: "60px",
          textAlign: "center",
          color: "#64748b",
          borderTop: "1px solid #e2e8f0",
          paddingTop: "20px",
          fontSize: "15px",
        }}
      >
        AI Proposal Automation • React • FastAPI • Gemini • ChromaDB • Machine
        Learning
      </footer>
    </div>
  );
}

export default App;