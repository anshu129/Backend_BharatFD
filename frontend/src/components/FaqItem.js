//Here are the contents for the file: /frontend/frontend/src/components/FaqItem.js

import React from 'react';

const FaqItem = ({ faq }) => {
    return (
        <div className="faq-item">
            <h3>{faq.question}</h3>
            <div dangerouslySetInnerHTML={{ __html: faq.answer }} />
        </div>
    );
};

export default FaqItem;