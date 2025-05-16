import { useRef, useState } from 'react';
import {
  ArrowLeftRight,
  CornerDownLeft,
  DiffIcon,
  DivideIcon,
  EqualIcon,
  MinusIcon,
  PercentIcon,
  PiIcon,
  PlusIcon,
  XIcon,
} from 'lucide-react';
import { cn } from '../lib/utils';
import { toast } from 'sonner';

const calculator_buttons = [
  [
    { label: 'C', value: 'clear', disabled: false, second: null },
    { label: <DiffIcon />, value: 'inv()', disabled: false, second: null },
    { label: 'xʸ', value: '^', disabled: false, second: null },
    { label: 'j', value: 'j', disabled: false, second: null },
    {
      label: '(',
      value: '(',
      disabled: false,
    },
    { label: '.', value: '.', disabled: false, second: null },
    {
      label: ')',
      value: ')',
      disabled: false,
    },
    { label: <DivideIcon />, value: '/', disabled: false, second: null },
  ],
  [
    { label: '7', value: '7', disabled: false, second: null },
    { label: '8', value: '8', disabled: false, second: null },
    { label: '9', value: '9', disabled: false, second: null },
    { label: <XIcon />, value: '*', disabled: false, second: null },
  ],
  [
    { label: '4', value: '4', disabled: false, second: null },
    { label: '5', value: '5', disabled: false, second: null },
    { label: '6', value: '6', disabled: false, second: null },
    { label: <MinusIcon />, value: '-', disabled: false, second: null },
  ],
  [
    { label: '1', value: '1', disabled: false, second: null },
    { label: '2', value: '2', disabled: false, second: null },
    { label: '3', value: '3', disabled: false, second: null },
    { label: <PlusIcon />, value: '+', disabled: false, second: null },
  ],
  [
    { label: '0', value: '0', disabled: false, second: null },
    { label: <EqualIcon />, value: '=', disabled: false, second: null },
  ],
];

export default function ClassicCalculator() {
  const [expression, setExpression] = useState('');
  const inputRef = useRef(null);

  const handleClick = async (value) => {
    const input = inputRef.current;
    input.focus();

    if (value === 'clear') {
      setExpression('');
    } else if (value === '=') {
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

  return (
    <>
      <input
        ref={inputRef}
        type="text"
        value={expression || ''}
        onChange={(e) => setExpression(e.target.value)}
        className="mb-4 p-4 w-full h-16 text-right text-2xl font-mono bg-gray-100 rounded focus-visible:outline-none"
      />

      <div className="grid w-full grid-cols-4 grid-rows-7 gap-2">
        {calculator_buttons.flat().map((btn, index) => {
          return (
            <button
              disabled={btn.disabled}
              key={index}
              onClick={() => handleClick(btn.value)}
              className={cn(
                'bg-white relative flex justify-center items-center border py-3 rounded hover:bg-gray-100 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white',
                btn.value === '0' && 'col-span-2',
                btn.value === '=' &&
                  'col-span-2 bg-black text-white hover:bg-black/80',
              )}
            >
              {btn.label}
            </button>
          );
        })}
      </div>
    </>
  );
}
