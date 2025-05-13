import { useEffect, useRef, useState } from 'react';
import { EqualIcon } from 'lucide-react';
import { toast } from 'sonner';

const MatrixInput = ({ matrix, setMatrix, rows, cols }) => {
  const handleChange = (rowIndex, colIndex, value) => {
    const newMatrix = matrix.map((row, i) =>
      row.map((cell, j) =>
        i === rowIndex && j === colIndex ? Number(value) : cell,
      ),
    );
    setMatrix(newMatrix);
  };

  return (
    <div
      className={`grid gap-2`}
      style={{ gridTemplateColumns: `repeat(${cols}, minmax(2rem, 1fr))` }}
    >
      {matrix.map((row, rowIndex) =>
        row.map((value, colIndex) => (
          <input
            key={`${rowIndex}-${colIndex}`}
            type="number"
            value={value}
            onChange={(e) => handleChange(rowIndex, colIndex, e.target.value)}
            className="border rounded px-2 py-1 text-center"
          />
        )),
      )}
    </div>
  );
};

export default function MatrixCalculator() {
  const [expression, setExpression] = useState('');
  const [operation, setOperation] = useState('+');
  const [matrixARows, setMatrixARows] = useState(2);
  const [matrixACols, setMatrixACols] = useState(2);
  const [matrixBRows, setMatrixBRows] = useState(2);
  const [matrixBCols, setMatrixBCols] = useState(2);
  const [matrixA, setMatrixA] = useState([
    [0, 0],
    [0, 0],
  ]);
  const [matrixB, setMatrixB] = useState([
    [0, 0],
    [0, 0],
  ]);
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
    setExpression(
      JSON.stringify(matrixA) + operation + JSON.stringify(matrixB),
    );
  }, [
    operation,
    matrixA,
    matrixB,
    matrixARows,
    matrixACols,
    matrixBRows,
    matrixBCols,
  ]);

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
          <div className="flex justify-start items-center gap-3">
            <span className="text-base font-medium">Operation</span>
            <select
              className="px-2 py-1 border rounded"
              value={operation}
              onChange={(e) => setOperation(e.target.value)}
            >
              <option>*</option>
              <option>+</option>
              <option>-</option>
            </select>
          </div>
          <button
            onClick={() => handleClick('=')}
            className="bg-black text-white row-span-2 flex justify-center items-center border py-2 px-3 rounded hover:bg-black/80 [&_svg]:size-4 disabled:text-gray-200 disabled:hover:bg-white"
          >
            <EqualIcon />
          </button>
        </div>

        <div className="flex flex-col space-y-2 w-full">
          <div className="flex justify-start items-center gap-3">
            <label className="font-semibold">Matrix A</label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                value={matrixARows}
                min={0}
                onChange={(e) => {
                  const newRowCount = parseInt(e.target.value, 10) || 0;
                  setMatrixARows(newRowCount);

                  setMatrixA((prev) => {
                    const updated = [...prev];

                    if (newRowCount > prev.length) {
                      for (let i = prev.length; i < newRowCount; i++) {
                        updated.push(
                          Array.from({ length: matrixACols }, () => 0),
                        );
                      }
                    } else if (newRowCount < prev.length) {
                      updated.length = newRowCount;
                    }

                    return updated;
                  });
                }}
                className="w-16 text-center border rounded"
              />
              <input
                type="number"
                value={matrixACols}
                min={0}
                onChange={(e) => {
                  const newColCount = parseInt(e.target.value, 10) || 0;
                  setMatrixACols(newColCount);

                  setMatrixA((prev) => {
                    return prev.map((row) => {
                      const updatedRow = [...row];

                      if (newColCount > row.length) {
                        for (let j = row.length; j < newColCount; j++) {
                          updatedRow.push(0);
                        }
                      } else if (newColCount < row.length) {
                        updatedRow.length = newColCount;
                      }

                      return updatedRow;
                    });
                  });
                }}
                className="w-16 text-center border rounded"
              />
            </div>
          </div>
          <MatrixInput
            matrix={matrixA}
            setMatrix={setMatrixA}
            rows={matrixARows}
            cols={matrixACols}
          />
        </div>

        <div className="flex flex-col space-y-2 w-full">
          <div className="flex justify-start items-center gap-3">
            <label className="font-semibold">Matrix B</label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                value={matrixBRows}
                min={0}
                onChange={(e) => {
                  const newRowCount = parseInt(e.target.value, 10) || 0;
                  setMatrixBRows(newRowCount);

                  setMatrixB((prev) => {
                    const updated = [...prev];

                    if (newRowCount > prev.length) {
                      for (let i = prev.length; i < newRowCount; i++) {
                        updated.push(
                          Array.from({ length: matrixBCols }, () => 0),
                        );
                      }
                    } else if (newRowCount < prev.length) {
                      updated.length = newRowCount;
                    }

                    return updated;
                  });
                }}
                className="w-16 text-center border rounded"
              />
              <input
                type="number"
                value={matrixBCols}
                min={0}
                onChange={(e) => {
                  const newColCount = parseInt(e.target.value, 10) || 0;
                  setMatrixBCols(newColCount);

                  setMatrixB((prev) => {
                    return prev.map((row) => {
                      const updatedRow = [...row];

                      if (newColCount > row.length) {
                        for (let j = row.length; j < newColCount; j++) {
                          updatedRow.push(0);
                        }
                      } else if (newColCount < row.length) {
                        updatedRow.length = newColCount;
                      }

                      return updatedRow;
                    });
                  });
                }}
                className="w-16 text-center border rounded"
              />
            </div>
          </div>
          <MatrixInput
            matrix={matrixB}
            setMatrix={setMatrixB}
            rows={matrixBRows}
            cols={matrixBCols}
          />
        </div>
      </div>
    </>
  );
}
