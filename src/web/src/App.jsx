import './App.css';
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
<<<<<<< Updated upstream
import {cn} from "./lib/utils.js";

const base_buttons = [
  [
    { label: '2nd', value: '2nd', disabled: false, second: null },
    { label: <PiIcon />, value: 'pi', disabled: true, second: { label: 'const', value: 'const' } },
    { label: 'e', value: 'e', disabled: true, second: { label: 'i', value: 'i' } },
    { label: '[::]', value: '[::]', disabled: true, second: null },
    { label: 'x', value: 'x', disabled: true, second: { label: '=', value: '=' } },
    { label: '(', value: '(', disabled: true, second: { label: '[', value: '[' } },
    { label: ',', value: ',', disabled: true, second: null },
    { label: ')', value: ')', disabled: true, second: { label: ']', value: ']' } },
    { label: <ArrowLeftRight />, value: 'swap', disabled: true, second: null },
    { label: <CornerDownLeft />, value: 'enter', disabled: true, second: null },
  ],
  [
    { label: 'sin', value: 'sin', disabled: true, second: { label: 'sin⁻¹', value: 'asin' }},
    { label: 'sinh', value: 'sinh', disabled: true, second: { label: 'sinh⁻¹', value: 'asinh' } },
    { label: 'cot', value: 'cot', disabled: true, second: { label: 'cot⁻¹', value: 'acot' } },
    { label: 'y√x', value: 'y_sqrt_x', disabled: true, second: null },
    { label: 'xʸ', value: 'x_pow_y', disabled: true, second: null },
    { label: '7', value: '7', disabled: false, second: null },
    { label: '8', value: '8', disabled: false, second: null },
    { label: '9', value: '9', disabled: false, second: null },
    { label: <DivideIcon />, value: '/', disabled: false, second: null },
    { label: 'C', value: 'clear', disabled: false, second: null },
  ],
  [
    { label: 'cos', value: 'cos', disabled: true, second: { label: 'cos⁻¹', value: 'acos' } },
    { label: 'cosh', value: 'cosh', disabled: true, second: { label: 'cosh⁻¹', value: 'acosh' } },
    { label: 'sec', value: 'sec', disabled: true, second: { label: 'sec⁻¹', value: 'asec' } },
    { label: '³√x', value: 'cbrt', disabled: true, second: null },
    { label: 'x³', value: 'x_cubed', disabled: true, second: null },
    { label: '4', value: '4', disabled: false, second: null },
    { label: '5', value: '5', disabled: false, second: null },
    { label: '6', value: '6', disabled: false, second: null },
    { label: <XIcon />, value: '*', disabled: false, second: null },
    { label: <EqualIcon />, value: '=', disabled: false, second: null },
  ],
  [
    { label: 'tan', value: 'tan', disabled: true, second: { label: 'tan⁻¹', value: 'atan' } },
    { label: 'tanh', value: 'tanh', disabled: true, second: { label: 'tanh⁻¹', value: 'atanh' } },
    { label: 'csc', value: 'csc', disabled: true, second: { label: 'csc⁻¹', value: 'acsc' } },
    { label: '√x', value: 'sqrt', disabled: true, second: null },
    { label: 'x²', value: 'x_squared', disabled: true, second: null },
    { label: '1', value: '1', disabled: false, second: null },
    { label: '2', value: '2', disabled: false, second: null },
    { label: '3', value: '3', disabled: false, second: null },
    { label: <MinusIcon />, value: '-', disabled: false, second: null },
  ],
  [
    { label: 'ncr', value: 'ncr', disabled: true, second: null },
    { label: 'npr', value: 'npr', disabled: true, second: null },
    { label: <PercentIcon />, value: '%', disabled: false, second: null },
    { label: 'log', value: 'log', disabled: true, second: null },
    { label: '10ˣ', value: '10_pow_x', disabled: true, second: null },
    { label: '0', value: '0', disabled: false, second: null },
    { label: <DiffIcon />, value: 'negate', disabled: false, second: null },
    { label: '.', value: '.', disabled: false, second: null },
    { label: <PlusIcon />, value: '+', disabled: false, second: null },
    { label: "=dec", value: 'toDec', disabled: true, second: null },
  ],
  [
    { label: 'or', value: 'or', disabled: true, second: null },
    { label: 'and', value: 'and', disabled: true, second: null },
    { label: "xor", value: 'xor', disabled: true, second: null },
    { label: 'ln', value: 'ln', disabled: true, second: null },
    { label: 'eˣ', value: 'e_pow_x', disabled: true, second: null },
    { label: 'A', value: 'A', disabled: true, second: null },
    { label: "B", value: 'B', disabled: true, second: null },
    { label: 'C', value: 'C', disabled: true, second: null },
    { label: '0b', value: '0b', disabled: true, second: null },
    { label: "=hex", value: 'toHex', disabled: true, second: null },
  ],
  [
    { label: 'lsh', value: 'rsh', disabled: true, second: { label: 'rol', value: 'rol' } },
    { label: 'rsh', value: 'rsh', disabled: true, second: { label: 'ror', value: 'ror' } },
    { label: '', value: '', disabled: true, second: null},
    { label: "lg2", value: 'lg2', disabled: true, second: null },
    { label: '2ˣ', value: '2_pow_x', disabled: true, second: null },
    { label: 'D', value: 'D', disabled: true, second: null },
    { label: 'E', value: 'E', disabled: true, second: null },
    { label: "F", value: 'F', disabled: true, second: null },
    { label: '0x', value: '0x', disabled: true, second: null },
    { label: "=bin", value: 'toBin', disabled: true, second: null },
  ],
];

export default function App() {
  const [second, setSecond] = useState(false);
  const [expression, setExpression] = useState('');
  const inputRef = useRef(null);

  const handleClick = (value) => {
    inputRef.current.focus();
    if (value === 'clear') {
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
      <div className="border max-w-3xl w-full rounded-lg bg-white flex flex-col p-4 shadow-xs">
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
        <div className="grid w-full grid-cols-10 grid-rows-7 gap-2">
          {base_buttons.flat().map((btn, index) => {
            if (btn.value === '=') {
              return (
                <button
                    disabled={btn.disabled}
                    key={index}
                    onClick={() => handleClick(btn.value)}
                    className="bg-black text-white row-span-2 flex justify-center items-center border py-2 rounded hover:bg-black/80 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
                >
                  {btn.label}
                </button>
              );
            }
            else if(btn.value === '2nd'){
              return (
                  <button
                      disabled={btn.disabled}
                      key={index}
                      onClick={() => setSecond(!second)}
                      className="bg-white flex justify-center items-center border py-3 rounded hover:bg-gray-100 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
                  >
                    {btn.label}
                  </button>
              )
            }
            else {
              if(second){
                return(
                    <button
                    disabled={btn.disabled}
                    key={index}
                    onClick={() => {
                      if(btn?.second){
                        handleClick(btn.second.value);
                      }else{
                        handleClick(btn.value);
                      }
                    }}
                    className={cn(
                        "bg-white relative flex justify-center items-center border py-3 rounded hover:bg-gray-100 disabled:text-gray-200 disabled:hover:bg-white",
                        btn?.second ? "[&_svg]:size-2.5": "[&_svg]:size-4"
                    )}
                >
                  {btn?.second ? btn.second.label: btn.label}
                  {btn?.second ? <span className="absolute top-0.5 right-1 font-medium text-[9px]">{btn.label}</span> : null}
                </button>
                )
              }else{
                return(
                    <button
                        disabled={btn.disabled}
                        key={index}
                        onClick={() => handleClick(btn.value)}
                        className="bg-white relative flex justify-center items-center border py-3 rounded hover:bg-gray-100 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
                    >
                      {btn.label}
                      {btn?.second ? <span className="absolute top-0.5 right-1 font-medium text-[9px]">{btn.second.label}</span> : null}
                    </button>
                );
              }
            }
          })}
        </div>
=======
import { cn } from './lib/utils.js';
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from './components/tabs.jsx';
import ClassicCalculator from './components/classic-calculator.jsx';
import MatrixCalculator from './components/matrix-calculator.jsx';

export default function App() {
  const [mode, setMode] = useState('classic');

  return (
    <div className="px-6 py-30 gap-20 grid grid-cols-2 bg-black/95 h-screen">
      <div className="border max-w-3xl h-fit w-full rounded-lg bg-white flex flex-col justify-start items-center p-4 shadow-xs">
        <div className="mb-6 flex justify-between items-center w-full">
          <h1 className="text-2xl font-semibold">Calculator Cucumber</h1>
          <div className="flex justify-end items-center">
            <button
              onClick={() => setMode('classic')}
              className="bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted"
            >
              Classic
            </button>
            <button
              onClick={() => setMode('matrix')}
              className="bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted"
            >
              Matrix
            </button>
          </div>
        </div>

        {mode === 'classic' && <ClassicCalculator />}
        {mode === 'matrix' && <MatrixCalculator />}

        <p className="mt-3 text-xs text-muted-foreground/40">
          By Arsène Mujyabwami, Ingrid Fondja Tchoumba, Nicolas Delplanque and
          Xavier Delabie{' '}
        </p>
      </div>
      <div className="flex flex-col gap-6 justify-start items-start h-full w-full bg-white rounded-md p-4">
        <p className="text-lg font-medium">Helper</p>
        <Tabs
          defaultValue="tab-1"
          orientation="vertical"
          className="w-full h-full flex flex-row"
        >
          <TabsList className="flex-col justify-start rounded-none border-l h-fit bg-transparent p-0">
            <TabsTrigger
              value="tab-1"
              className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
            >
              Classic
            </TabsTrigger>
            <TabsTrigger
              value="tab-2"
              className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
            >
              Matrix
            </TabsTrigger>
            <TabsTrigger
              value="tab-3"
              className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
            >
              ?
            </TabsTrigger>
          </TabsList>
          <div className="grow rounded-md border text-start">
            <TabsContent
              value="tab-1"
              className="py-3 px-4 grid gap-3 grid-cols-2"
            >
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Infix</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Addition :</span> a + b
                  </p>
                  <p>
                    <span className="font-bold">Subtraction :</span> a - b
                  </p>
                  <p>
                    <span className="font-bold">Multiplication :</span> a * b
                  </p>
                  <p>
                    <span className="font-bold">Division :</span> a / b
                  </p>
                  <p>
                    <span className="font-bold">Exponentiation :</span> a ^ b
                  </p>
                  <p>
                    <span className="font-bold">Negation :</span> (-a)
                  </p>
                  <p>
                    <span className="font-bold">Inverse :</span> inv(a)
                  </p>
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Prefix</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Addition :</span> +(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    +(a b)
                  </p>
                  <p>
                    <span className="font-bold">Subtraction :</span> -(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    -(a b)
                  </p>
                  <p>
                    <span className="font-bold">Multiplication :</span> *(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    *(a b)
                  </p>
                  <p>
                    <span className="font-bold">Division :</span> /(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    /(a b)
                  </p>
                  <p>
                    <span className="font-bold">Exponentiation :</span> ^(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    ^(a b)
                  </p>
                  <p>
                    <span className="font-bold">Negation :</span> (-(a))
                  </p>
                  <p>
                    <span className="font-bold">Inverse :</span> inv(a)
                  </p>
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Postfix</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Addition :</span> (a, b)+{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)+
                  </p>
                  <p>
                    <span className="font-bold">Subtraction :</span> (a, b)-{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)-
                  </p>
                  <p>
                    <span className="font-bold">Multiplication :</span> (a, b)*{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)*
                  </p>
                  <p>
                    <span className="font-bold">Division :</span> (a, b)/{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)/
                  </p>
                  <p>
                    <span className="font-bold">Exponentiation :</span> (a, b)^{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)^
                  </p>
                  <p>
                    <span className="font-bold">Negation :</span> (a-)-
                  </p>
                  <p>
                    <span className="font-bold">Inverse :</span> inv(a)
                  </p>
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Others</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Multiple operands :</span> +(a,
                    b, c)
                  </p>
                  <p>
                    <span className="font-bold">Nested operations :</span> *(a,
                    +(b, c))
                  </p>
                  <p>
                    <span className="font-bold">Complex numbers :</span> a + bj
                  </p>
                  <p>
                    <span className="font-bold">Parentheses :</span> (a + b) * c
                  </p>
                </div>
              </div>
            </TabsContent>
            <TabsContent value="tab-2">
              <p className="text-muted-foreground px-4 py-3 text-xs">
                Content for Tab 2
              </p>
            </TabsContent>
            <TabsContent value="tab-3">
              <p className="text-muted-foreground px-4 py-3 text-xs">
                Content for Tab 3
              </p>
            </TabsContent>
          </div>
        </Tabs>
>>>>>>> Stashed changes
      </div>
    </div>
  );
}
