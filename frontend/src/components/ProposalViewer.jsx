import React from "react";

const API_BASE = import.meta.env.VITE_API_URL;

function StatCard({ icon, title, value }) {
    return (
        <div
            style={{
                flex: 1,
                minWidth: "180px",
                background: "#ffffff",
                border: "1px solid #e5e7eb",
                borderRadius: "12px",
                padding: "18px",
                boxShadow: "0 2px 8px rgba(0,0,0,.05)",
            }}
        >
            <div style={{ fontSize: "28px" }}>{icon}</div>

            <div
                style={{
                    color: "#64748b",
                    marginTop: "8px",
                    fontSize: "14px",
                }}
            >
                {title}
            </div>

            <div
                style={{
                    fontWeight: "bold",
                    fontSize: "18px",
                    marginTop: "6px",
                }}
            >
                {value || "-"}
            </div>
        </div>
    );
}

function ProposalViewer({
    proposal,
    analysis,
    similarProjects,
    docxDownload,
    pdfDownload,
}) {
    if (!proposal) return null;

    return (
        <div
            style={{
                marginTop: "40px",
                background: "#f8fafc",
                borderRadius: "18px",
                padding: "30px",
                boxShadow: "0 8px 24px rgba(0,0,0,.08)",
            }}
        >
            <div
                style={{
                    background: "#dcfce7",
                    color: "#166534",
                    padding: "14px",
                    borderRadius: "10px",
                    fontWeight: "600",
                    marginBottom: "25px",
                }}
            >
                ✅ Proposal Generated Successfully
            </div>

            <h2>🤖 AI Requirement Analysis</h2>

            <div
                style={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: "15px",
                    marginTop: "20px",
                    marginBottom: "35px",
                }}
            >
                <StatCard icon="🌍" title="Domain" value={analysis?.domain} />
                <StatCard icon="⚙️" title="Complexity" value={analysis?.complexity} />
                <StatCard icon="⏳" title="Timeline" value={analysis?.timeline} />
                <StatCard icon="💰" title="Budget" value={analysis?.budget} />
            </div>

            <h2>📚 Similar Projects</h2>

            {similarProjects?.length ? (
                similarProjects.map((project, index) => (
                    <div
                        key={index}
                        style={{
                            background: "#fff",
                            border: "1px solid #e5e7eb",
                            borderRadius: "12px",
                            padding: "20px",
                            marginTop: "15px",
                        }}
                    >
                        <h3>📌 {project.title}</h3>

                        <p>
                            <strong>🌍 Domain:</strong> {project.domain}
                        </p>

                        <p>
                            <strong>📝 Summary:</strong> {project.summary}
                        </p>

                        <p>
                            <strong>💻 Tech Stack:</strong>{" "}
                            {Array.isArray(project.tech_stack)
                                ? project.tech_stack.join(", ")
                                : project.tech_stack}
                        </p>
                    </div>
                ))
            ) : (
                <p>No similar projects found.</p>
            )}

            <h2 style={{ marginTop: "35px" }}>📥 Downloads</h2>

            <div
                style={{
                    display: "flex",
                    gap: "15px",
                    marginBottom: "30px",
                }}
            >
                {docxDownload && (
                    <a
                        href={`${API_BASE}/${docxDownload}`}
                        target="_blank"
                        rel="noreferrer"
                    >
                        <button
                            style={{
                                padding: "12px 20px",
                                border: "none",
                                borderRadius: "8px",
                                background: "#2563eb",
                                color: "#fff",
                                cursor: "pointer",
                            }}
                        >
                            ⬇ Download DOCX Proposal
                        </button>
                    </a>
                )}

                {pdfDownload && (
                    <a
                        href={`${API_BASE}/${pdfDownload}`}
                        target="_blank"
                        rel="noreferrer"
                    >
                        <button
                            style={{
                                padding: "12px 20px",
                                border: "none",
                                borderRadius: "8px",
                                background: "#dc2626",
                                color: "#fff",
                                cursor: "pointer",
                            }}
                        >
                            ⬇ Download PDF Proposal
                        </button>
                    </a>
                )}
            </div>

            <h2>📄 Generated Proposal</h2>

            <div
                style={{
                    background: "#fff",
                    border: "1px solid #e5e7eb",
                    borderRadius: "12px",
                    padding: "25px",
                    whiteSpace: "pre-wrap",
                    lineHeight: "1.8",
                    maxHeight: "700px",
                    overflowY: "auto",
                    fontFamily: "Segoe UI, sans-serif",
                }}
            >
                {proposal}
            </div>
        </div>
    );
}

export default ProposalViewer;