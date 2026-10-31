import { useState } from "react";
import API from "../services/api";

function UploadBox({
    setProposal,
    setAnalysis,
    setSimilarProjects,
    setDocxDownload,
    setPdfDownload
}) {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const uploadFile = async () => {

        if (!file) {
            alert("Please select a PDF first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {

            setLoading(true);

            const res = await API.post("/upload-pdf", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });

            // Clear previous data
            setProposal("");
            setAnalysis(null);
            setSimilarProjects([]);
            setDocxDownload("");
            setPdfDownload("");

            // Update with new data
            setProposal(res.data.proposal);
            setAnalysis(res.data.analysis);
            setSimilarProjects(res.data.similar_projects || []);
            setDocxDownload(res.data.docx_download || "");
            setPdfDownload(res.data.pdf_download || "");

        } catch (err) {

            console.error(err);

            // Clear old results
            setProposal("");
            setAnalysis(null);
            setSimilarProjects([]);
            setDocxDownload("");
            setPdfDownload("");

            if (err.response?.data?.detail) {
                alert(err.response.data.detail);
            } else {
                alert("Something went wrong while processing the PDF.");
            }

        } finally {

            setLoading(false);

        }
    };

    return (
        <div
            style={{
                marginTop: "35px",
                padding: "25px",
                background: "#ffffff",
                borderRadius: "12px",
                boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
            }}
        >

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <br /><br />

            <button
                onClick={uploadFile}
                disabled={loading}
                style={{
                    padding: "12px 28px",
                    fontSize: "16px",
                    border: "none",
                    borderRadius: "8px",
                    background: "#2563eb",
                    color: "white",
                    cursor: loading ? "not-allowed" : "pointer"
                }}
            >
                {loading ? "Generating Proposal..." : "Generate Proposal"}
            </button>

        </div>
    );
}

export default UploadBox;