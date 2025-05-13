import { useEffect, useRef, useState } from 'react';
import { EqualIcon } from 'lucide-react';
import { toast } from 'sonner';

const EquationInput = ({ equations, setEquations }) => {
  const handleChange = (index, value) => {
    const newEquations = equations.map((eq, i) => (i === index ? value : eq));
    setEquations(newEquations);
  };

  return (
    <div className="flex flex-col space-y-2">
      {equations.map((equation, index) => (
        <input
          key={index}
          type="text"
          value={equation}
          onChange={(e) => handleChange(index, e.target.value)}
          className="border rounded px-2 py-1 text-start"
          placeholder={`Équation ${index}`}
        />
      ))}
    </div>
  );
};

export default function EquationCalculator() {
  const [expression, setExpression] = useState('');
  const [numberOfEquations, setNumberOfEquations] = useState(2);
  const [equations, setEquations] = useState(Array(numberOfEquations).fill(''));
  const inputRef = useRef(null);

  const handleClick = async (value) => {
    const input = inputRef.current;
    input.focus();

    if (value === '=') {
      try {
        const response = await fetch('http://localhost:8000/api/calculate/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ expression }),
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
    } else {
      const start = input.selectionStart;
      const end = input.selectionEnd;

      const newExpression =
        expression.slice(0, start) + value + expression.slice(end);

      setExpression(newExpression);

      setTimeout(() => {
        input.selectionStart = input.selectionEnd = start + value.length;
      }, 0);
    }
  };

  useEffect(() => {
    const allFilled = equations.every((eq) => eq.trim() !== '');

    if (equations.length > 0 && allFilled) {
      const formatted = equations.map((eq) => eq.trim()).join('; ');
      setExpression(`solve_linear("${formatted}")`);
    }
  }, [equations]);

  return (
    <>
      <input
        ref={inputRef}
        type="text"
        value={expression || ''}
        onChange={(e) => setExpression(e.target.value)}
        className="mb-4 p-4 w-full h-16 text-right text-2xl font-mono bg-gray-100 rounded focus-visible:outline-none"
      />
      <div className="flex flex-col w-full items-start justify-start gap-4">
        <div className="flex w-full justify-between items-center">
          <p className="text-base font-medium">Equation Solver</p>
          <div className="flex justify-end gap-3 items-center">
            <p className="text-sm font-normal">Number of equations</p>
            <input
              className="w-20 border py-1 px-3 rounded-md"
              type="number"
              value={numberOfEquations}
              onChange={(e) => {
                const newCount = parseInt(e.target.value, 10);
                setNumberOfEquations(newCount);

                setEquations((prev) => {
                  if (newCount > prev.length) {
                    return [...prev, ...Array(newCount - prev.length).fill('')];
                  } else {
                    return prev.slice(0, newCount);
                  }
                });
              }}
            />
            <button
              onClick={() => handleClick('=')}
              className="bg-black text-white row-span-2 flex justify-center items-center border py-2 px-3 rounded hover:bg-black/80 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
            >
              <EqualIcon />
            </button>
          </div>
        </div>

        <div className="flex flex-col space-y-2 w-full">
          <EquationInput equations={equations} setEquations={setEquations} />
        </div>
      </div>
    </>
  );
}
