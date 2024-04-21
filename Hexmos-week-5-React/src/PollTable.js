
import React, { useState, useEffect, useContext } from 'react';
import {useNavigate} from "react-router-dom";

import SelectedTagsContext from './SelectedTagsContext';


function PollTable() {
  const [polls, setPolls] = useState([]);
  const [error, setError] = useState(null);
  const navigate=useNavigate();
  const {Tags,filterByTags,updateFilterByTags,getAllPolls,updateGetAllPolls} = useContext(SelectedTagsContext);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/polls/get_polls/')
      .then(response => {
        if(!response.ok){
          throw new Error('Failed to fetch polls');
        }
        return response.json();
      })

      .then(data => setPolls(data))
      .catch(error => {
        setError(error.message);
        console.error('Error fetching polls:', error);
      });
  }, [getAllPolls]);

  
  
  useEffect(() => {
    if(filterByTags){
        fetch(`http://127.0.0.1:8000/polls/get_polls_by_tags/?tags=${Tags}`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to fetch polls');
          }
          return response.json();
        })
        .then(data => setPolls(data))
        .catch(error => {
          setError(error.message);
          console.error('Error fetching polls:', error);
        });
      }
      updateGetAllPolls(false);
      updateFilterByTags(false);
  }, [ Tags,filterByTags,updateFilterByTags]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div class="table" id="pg1table">
      <table class="table" ALIGN="right">
        <thead>
          <tr class="first-row">
            <th>Number</th>
            <th> Poll Question</th>
            <th> Total votes</th>
            <th>Tags</th>
          </tr>
        </thead>
        <tbody>
          {polls.map((poll,index)=> (
            <tr key={poll.Question_ID}>
              <td>{index+1}</td>
              <td onClick={ () => navigate({
                  pathname: '/PollDetail',
                  search: `?id=${poll.Question_ID}`,
              })}>{poll.Question}</td>
              <td>{Object.values(poll.OptionVote).reduce((acc, curr) => acc + parseInt(curr), 0)}</td>
              <td>{poll.Tags.join(', ')}</td>
              
            </tr>
          ))}
        </tbody>
      </table>
      
    </div>
  );
};
 

export default PollTable;





