import gql from 'graphql-tag'

export default gql`
    mutation createPoint($details: String!, $number: Int!, $points_owner_id: String!)
      {
      putPoint(input: {details: $details, number: $number, points_owner_id: $points_owner_id})
      {id, details}
      }
    `
