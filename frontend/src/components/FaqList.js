import React, { useEffect, useState } from 'react';
import { fetchFAQs } from '../services/api';
import FaqItem from './FaqItem';

const FaqList = () => {
    const [faqs, setFaqs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getFAQs = async () => {
            try {
                const data = await fetchFAQs();
                setFaqs(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        getFAQs();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Frequently Asked Questions</h1>
            <ul>
                {faqs.map(faq => (
                    <FaqItem key={faq.id} faq={faq} />
                ))}
            </ul>
        </div>
    );
};

export default FaqList;