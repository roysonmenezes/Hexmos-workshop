import React, { useState, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom'; // Import useParams
import Heading from './Heading';

// import {Pie} from 'react-chartjs-2'
import { Piechart } from './Piechart';

function PollDetail() {
 const [poll, setPolls] = useState([]);
 const [error, setError] = useState(null);
 
 const [searchParams]=useSearchParams();
 const idString=searchParams.get('id');
 const poll_id=Number(idString);
 const navigate=useNavigate();

//  for piechart
// const [chartData,setChartData]=useState(null)

 useEffect(() => {
    fetch(`http://127.0.0.1:8000/polls/${poll_id}/get_polls_by_id/`)
      .then(response => response.json())
      .then(data => setPolls(data))
      .catch(error => {
        setError(error.message);
        console.error('Error fetching polls:', error);
      });
 }, [poll_id]);

 if (error) {
    return <div>Error: {error}</div>;
 }

 // Ensure poll has the expected structure before rendering
 if (!poll.Question || !poll.OptionVote || !poll.Tags) {
    return <div>Loading...</div>;
 }
 const options={
  data:[
    ["Options","Votes"],
    ...Object.entries(poll.OptionVote)
  ],
  title:{
    title:"Poll votes "
  }
 };

 const Votes=Object.values(poll.OptionVote).reduce((acc, curr) => acc + parseInt(curr), 0)
 return (
  <div>
    <Heading/>
    <h1 className="heading">{poll.Question}</h1>
    <button class="btn-normal" id="btn-pg2" onClick={ () => navigate({
        pathname:'/Vote',
        search: `?id=${poll.Question_ID}`,
      })}>Vote on this poll</button>
    <div className="table" id="pg2table">
      
      <table className="table" align="right">
        <thead>
          <tr className="first-row">
            <th>Number</th>
            <th>Option</th>
            <th>Votes</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(poll.OptionVote).map(([option, votes]) => (
            <tr key={option}>
              <td>{Object.keys(poll.OptionVote).indexOf(option) + 1}</td>
              <td>{option}</td>
              <td>{votes}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p className="para">Tags: {poll.Tags.join(', ')}</p>
    </div>
    {Votes > 0 &&
      <Piechart option={options}/>
    };
    

    
  </div>
 );
}

export default PollDetail;;
