import { useState } from 'react';

function Input({ placeholder, name, value, onChange }) {
    return (
        <input
            type="text"
            placeholder={placeholder}
            name={name}
            value={value}
            onChange={onChange}
        />
    );
}

function HandleNewProductForm({ refetch }) {
    const [formData, setFormData] = useState({
        product_name: "",
        nutri_score: "",
        nova_score: "",
        green_score: ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch("/data", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData),
            });

            if (!response.ok) throw new Error("Petition error");

            await response.json();
            refetch();
        } catch (err) {
            console.error("Error:", err);
        } finally {
            // netegem inputs
            setFormData({
                product_name: "",
                nutri_score: "",
                nova_score: "",
                green_score: ""
            });
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Product's name:</label><br />
            <Input placeholder="New product" name="product_name" value={formData.product_name} onChange={handleChange} /><br />

            <label>Nutri score:</label><br />
            <Input placeholder="Nutri score" name="nutri_score" value={formData.nutri_score} onChange={handleChange} /><br />

            <label>Nova score:</label><br />
            <Input placeholder="Nova score" name="nova_score" value={formData.nova_score} onChange={handleChange} /><br />

            <label>Green score:</label><br />
            <Input placeholder="Green score" name="green_score" value={formData.green_score} onChange={handleChange} /><br />

            <button type="submit">Submit</button>
        </form>
    );
}

export default HandleNewProductForm;