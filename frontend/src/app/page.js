"use client";
import { useEffect, useState } from "react";
import Image from "next/image";

export default function Home() {
  const [items, setItems] = useState([]);
  const [title, setTitle] = useState("");
  const [before, setBefore] = useState(null);
  const [after, setAfter] = useState(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/portfolio/`)
      .then((res) => res.json())
      .then(setItems);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!before || !after) return;

    const formData = new FormData();
    formData.append("title", title);
    formData.append("before_image", before);
    formData.append("after_image", after);

    await fetch(`${process.env.NEXT_PUBLIC_API_URL}/portfolio/`, {
      method: "POST",
      body: formData,
    });

    setTitle("");
    setBefore(null);
    setAfter(null);

    const refreshed = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/portfolio/`).then(res => res.json());
    setItems(refreshed);
  };

  return (
    <main className="max-w-3xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Before/After Portfolio</h1>

      <div className="grid gap-6">
        {items.map((item) => (
          <div key={item.id} className="p-4 border rounded shadow">
            <h2 className="font-semibold mb-2">{item.title}</h2>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-gray-500 mb-1">Before</p>
                <Image width={100} height={100} src={item.before_image} alt="before" className="rounded" />
              </div>
              <div>
                <p className="text-sm text-gray-500 mb-1">After</p>
                <Image width={100} height={100} src={item.after_image} alt="after" className="rounded" />
              </div>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
