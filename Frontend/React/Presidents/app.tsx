import React, { useEffect, useState } from "react";


const App = () => {
  const [presidents, setPresidents] = useState([]);
  const [sort, setSort] = useState({ sort: 'ASC', field: 'number' });

  const fetchData = async () => {
    const data = await fetch(`https://raw.githubusercontent.com/hitch17/sample-data/master/presidents.json`);
    const fetched = await data.json();
    const sorted = fetched.map((pres) => {
      return {
        ...pres,
        death_year: pres.death_year === null ? 2023 : pres.death_year
      }
    })
    setPresidents(sorted);
  }

  const handleSort = (field) => {
    if (field === sort.field) {
      setSort({ sort: sort.sort === 'ASC' ? 'DESC' : 'ASC', field: field });
    } else {
      setSort({ sort: 'ASC', field: field });
    }
    if (field === 'number' || field === 'birth_year' || field === 'death_year') {
      const temp = presidents.sort((a, b) => {
        return sort.sort === 'ASC' ? a[field] - b[field] : b[field] - a[field];
      })
      setPresidents(temp);
    }
    if (field === 'president' || field === 'party') {
      const temp = presidents.sort((a, b) => {
        if (a[field] < b[field]) return sort.sort === 'ASC' ? -1 : 1;
        if (a[field] > b[field]) return sort.sort === 'ASC' ? 1 : -1;
        return 0;
      })
      setPresidents(temp);
    }
    if (field === 'took_office' || field === 'left_office') {
      const temp = presidents.sort((a, b) => {

        return sort.sort === 'ASC' ? new Date(a[field]).valueOf() - new Date(b[field]).valueOf() : new Date(b[field]).valueOf() - new Date(a[field]).valueOf();
      })
      console.log(temp);
      setPresidents(temp);
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      {presidents ? (<table>
        <tr className="columns">
          <th onClick={() => handleSort('number')}>number{sort.field === 'number' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
          <th onClick={() => handleSort('president')}>president{sort.field === 'president' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
          <th onClick={() => handleSort('birth_year')}>birth_year{sort.field === 'birth_year' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
          <th onClick={() => handleSort('death_year')}>death_year{sort.field === 'death_year' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
          <th onClick={() => handleSort('took_office')}>took_office{sort.field === 'took_office' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
          <th onClick={() => handleSort('left_office')}>left_office{sort.field === 'left_office' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
          <th onClick={() => handleSort('party')}>party{sort.field === 'party' && (sort.sort === 'ASC' ? <>&uarr;</> : <>&darr;</>)}</th>
        </tr>
        {presidents.map((pres) => {
          return (
            <tr>
              <th>{pres.number}</th>
              <th>{pres.president}</th>
              <th>{pres.birth_year}</th>
              <th>{pres.death_year === 2023 ? 'Alive' : pres.death_year}</th>
              <th>{pres.took_office}</th>
              <th>{pres.left_office}</th>
              <th>{pres.party}</th>
            </tr>
          )
        })}
      </table>) : 'Loading'}
    </>
  )
}
export default App;