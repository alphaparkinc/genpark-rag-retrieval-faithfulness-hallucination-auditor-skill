from client import RagRetrievalFaithfulnessHallucinationAuditorClient

def main():
    client = RagRetrievalFaithfulnessHallucinationAuditorClient()
    res = client.audit_rag_generation(['Fast refund policy within 30 days.'], 'Refunds are allowed for 60 days.')
    print('RAG Faithfulness Auditor: ' + res['rag_audit_id'] + ' (Faithfulness: ' + str(res['faithfulness_score_pct']) + '%)')
    print('Hallucination: ' + str(res['hallucination_detected']) + ' | Relevancy: ' + str(res['answer_relevancy_score']))
    print('Dossier URL: ' + res['evaluation_audit_dossier_url'])

if __name__ == '__main__':
    main()
