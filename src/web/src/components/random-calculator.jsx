import { useRef, useState } from 'react';
import { EqualIcon } from 'lucide-react';
import { toast } from 'sonner';

export default function RandomCalculator() {
  const [expression, setExpression] = useState('');
  const inputRef = useRef(null);

  const handleClick = async (value) => {
    const input = inputRef.current;
    input.focus();

    try {
      const response = await fetch('http://localhost:8000/api/calculate/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression: value }),
      });

      if (!response.ok) {
        toast.error('Error during the assessment. Check your expression !');
      } else {
        const data = await response.json();
        setExpression(String(data.result));
      }
    } catch (error) {
      console.error(error);
      toast.error('Request error. Check if the backend is online !');
    }
  };

  return (
    <>
      <input
        ref={inputRef}
        type="text"
        readOnly
        value={expression || ''}
        className="mb-4 p-4 w-full h-16 text-right text-2xl font-mono bg-gray-100 rounded focus-visible:outline-none"
      />

      <div className="grid w-full grid-cols-3 grid-rows-7 gap-2">
        <button
          onClick={() => handleClick('random1')}
          className="bg-white flex justify-center items-center border py-1.5 px-3 rounded hover:bg-gray-100 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
        >
          Random Integer
        </button>
        <button
          onClick={() => handleClick('random2')}
          className="bg-white flex justify-center items-center border py-1.5 px-3 rounded hover:bg-gray-100 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
        >
          Random Rational
        </button>
        <button
          onClick={() => handleClick('random3')}
          className="bg-white flex justify-center items-center border py-1.5 px-3 rounded hover:bg-gray-100 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
        >
          Random Complex
        </button>
      </div>
    </>
  );
}
