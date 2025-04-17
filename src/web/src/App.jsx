import './App.css';
import { useRef, useState } from 'react';
import {
  DiffIcon,
  DivideIcon,
  EqualIcon,
  MinusIcon,
  PercentIcon,
  PlusIcon,
  XIcon,
} from 'lucide-react';

const base_buttons = [
  [
    { label: 'C', value: 'C' },
    { label: <DiffIcon />, value: '?' },
    { label: <PercentIcon />, value: '?' },
    { label: <DivideIcon />, value: '/' },
  ],
  [
    { label: '7', value: '7' },
    { label: '8', value: '8' },
    { label: '9', value: '9' },
    { label: <XIcon />, value: '*' },
  ],
  [
    { label: '4', value: '4' },
    { label: '5', value: '5' },
    { label: '6', value: '6' },
    { label: <MinusIcon />, value: '-' },
  ],
  [
    { label: '1', value: '1' },
    { label: '2', value: '2' },
    { label: '3', value: '3' },
    { label: <PlusIcon />, value: '+' },
  ],
  [
    { label: '0', value: '0' },
    { label: ',', value: ',' },
    { label: <EqualIcon />, value: '=' },
  ],
];

export default function App() {
  const [expression, setExpression] = useState('');
  const inputRef = useRef(null);

  const handleClick = (value) => {
    inputRef.current.focus();
    if (value === 'C') {
      setExpression('');
    } else if (value === '=') {
      try {
        //TODO: Send the expression to the API for evaluation
        const result = eval(
          expression.replace(/÷/g, '/').replace(/x/g, '*').replace(/-/g, '-'),
        );
        setExpression(result.toString());
      } catch {
        setExpression('Erreur');
      }
    } else {
      setExpression(expression + value);
    }
  };

  return (
    <div className="p-4 flex bg-black/95 justify-center items-center h-screen">
      <div className="border max-w-xl rounded-lg bg-white flex flex-col p-4 shadow-xs">
        <h1 className="text-2xl font-semibold text-center mb-6">
          Calculator Cucumber
        </h1>
        <input
          ref={inputRef}
          type="text"
          value={expression || '0'}
          className="mb-4 p-4 w-full h-16 text-right text-2xl font-mono bg-gray-100 rounded focus-visible:outline-none"
          readOnly
        />
        <div className="grid w-full grid-cols-4 gap-2">
          {base_buttons.flat().map((btn, index) => {
            if (btn.value === '0') {
              return (
                <button
                  key={index}
                  onClick={() => handleClick(btn.value)}
                  className="bg-white col-span-2 flex justify-center items-center border py-2 rounded hover:bg-gray-100 [&_svg]:size-4"
                >
                  {btn.label}
                </button>
              );
            } else {
              return (
                <button
                  key={index}
                  onClick={() => handleClick(btn.value)}
                  className="bg-white flex justify-center items-center border py-2 rounded hover:bg-gray-100 [&_svg]:size-4"
                >
                  {btn.label}
                </button>
              );
            }
          })}
        </div>
      </div>
    </div>
  );
}
